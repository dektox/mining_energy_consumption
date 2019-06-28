# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:11:26 2019

@author: Anton
"""
import logging
from datetime import datetime
import sqlite3

LOGGER = logging.getLogger()
# Logging
LOGGER.setLevel('INFO')
# Console outputs
LOGGER.addHandler(logging.StreamHandler())

#connecting to DBs, downloading data
conn = sqlite3.connect('data.db')
conn2 = sqlite3.connect('miners.db')
conn3 = sqlite3.connect('energy.db')
c = conn.cursor()
c2 = conn2.cursor()
c3 = conn3.cursor()

c.execute('SELECT * FROM prof_threshold')
prof_threshold=c.fetchall()

c.execute('SELECT * FROM hash_rate')
hash_rate=c.fetchall()

c2.execute('SELECT * FROM miners')
miners=c2.fetchall()

# Creating table. timestamp is a PRIMARY KEY, values are unique
c3.execute(f"CREATE TABLE IF NOT EXISTS energy_consumption"
               f" (timestamp INT PRIMARY KEY, date TEXT, max_consumption REAL, min_consumption REAL, guess_consumption REAL, all_prof_eqp TEXT, all_prof_eqp_qty TEXT);")
inserted_count = 0
# Template of the query to paste a row to a table
insert_sql = f"INSERT INTO energy_consumption ('timestamp', 'date', 'max_consumption', 'min_consumption', 'guess_consumption', 'all_prof_eqp', 'all_prof_eqp_qty') VALUES (?, ?, ?, ?, ?, ?, ?);"

prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment
prof_eqp_all = []  # list of lists of profitable equipment efficiency [for all dates]
prof_eqp_qty = []  # temprorary var for the list of profitable equipment qty -- neded for weighting
prof_eqp_qty_all = [] # list of lists of profitable equipment qty [for all dates]
max_consumption_all = []
min_consumption_all = []
guess_consumption_all = []
prof_threshold_avg = 0
MA = 30 #that is amount of days to calculate the moving average of profitability threshold, 1 for no averaging

# for EACH time period do:
for i in range(100, len(prof_threshold)):
    # calculate the MA of prof_threshold:
    for k in range(0,MA):
        prof_threshold_avg=prof_threshold_avg+prof_threshold[i-k][2]
    prof_threshold_avg=prof_threshold_avg/MA
    # check if EACH miner in our DB was profitable this day or not:
    for miner in miners:
        if prof_threshold[i][0]>miner[1] and prof_threshold_avg>miner[2]: 
        # ^^current date and date of miner release ^^checks if miner is profitable; 
        # if yes, adds miner's efficiency and qty to the lists:
            prof_eqp.append(miner[2])
            prof_eqp_qty.append(miner[3])
    prof_eqp_qty_all.append(prof_eqp_qty)
    prof_eqp_all.append(prof_eqp)
    try:        
        max_consumption = max(prof_eqp)*hash_rate[i][2]*1000*60*60/3.6e+15
        min_consumption = min(prof_eqp)*hash_rate[i][2]*1000*60*60/3.6e+15
        weighted_sum = 0
        eqp_qty_this_day = 0
        # calculating the guess_consumption using the weighted average of prof_eqp efficiencies:
        for j in range(0, len(prof_eqp)):
            weighted_sum = weighted_sum + prof_eqp[j]*prof_eqp_qty[j]
            eqp_qty_this_day = eqp_qty_this_day + prof_eqp_qty[j]
        guess_consumption = weighted_sum/eqp_qty_this_day*hash_rate[i][2]*1000*365.25*24*60*60/3.6e+15
    except: #in case if mining is not profitable (it is impossible to find MIN or MAX of empty list):
        max_consumption = max_consumption_all[-1]
        min_consumption = min_consumption_all[-1]
        guess_consumption = guess_consumption_all[-1]
    max_consumption_all.append(max_consumption)
    min_consumption_all.append(min_consumption)
    guess_consumption_all.append(guess_consumption)
    timestamp = prof_threshold[i][0]
    date = prof_threshold[i][1]
    prof_eqp = str(prof_eqp).strip('[]') #making str from prof_eqp
    prof_eqp_qty = str(prof_eqp_qty).strip('[]')
    try:
        c3.execute(insert_sql, (timestamp, date, max_consumption, min_consumption, guess_consumption, prof_eqp, prof_eqp_qty))
    # If the row with this timestamp already exist, ignore it:
    except sqlite3.IntegrityError:
        pass
    else:
        inserted_count += 1
    prof_eqp = []
    prof_eqp_qty = []
    prof_threshold_avg = 0
    
LOGGER.info(f"ENERGY: Saved {inserted_count} new values on {datetime.utcnow().isoformat()}")            
#closing connections to DBs
conn.close()
conn2.close()
conn3.commit()
conn3.close()
