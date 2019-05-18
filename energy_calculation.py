# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:11:26 2019

@author: Anton
"""
import sqlite3

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
               f" (timestamp INT PRIMARY KEY, date TEXT, max_consumption REAL, min_consumption REAL, guess_consumption REAL);")
inserted_count = 0
# Template of the query to paste a row to a table
insert_sql = f"INSERT INTO energy_consumption ('timestamp', 'date', 'max_consumption', 'min_consumption', 'guess_consumption') VALUES (?, ?, ?, ?, ?);"

prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment
exist_eqp = []  # temprorary var for the list of existing equipment efficiency at moment when mining is not profitable
max_consumption = [] 
min_consumption = []
guess_consumption = []
all_prof_eqp = []  # list of lists of profitable equipment efficiency in all the dates
all_exist_eqp = [] # list of lists of all existing equipment efficiency in all the dates when mining is not profitable

# for EACH time period for EACH miner do:
for i in range(0, len(prof_threshold)):
    for miner in miners:
        if prof_threshold[i][0]>miner[1] and prof_threshold[i][2]>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    all_prof_eqp.append(prof_eqp)
    try:
        max_consumption = max(prof_eqp)*hash_rate[i][2]*1000*364.24*24*60*60/3600000000000000
        min_consumption = min(prof_eqp)*hash_rate[i][2]*1000*364.24*24*60*60/3600000000000000
        guess_consumption = sum(prof_eqp)/len(prof_eqp)*hash_rate[i][2]*1000*364.24*24*60*60/3600000000000000    
    except: #in case if mining is not profitable (it is impossible to find MIN or MAX of empty list)
        for miner in miners:
            if prof_threshold[i][0]>miner[1]: exist_eqp.append(miner[2])
        all_exist_eqp.append(exist_eqp)
        unprof_consumption = sum(exist_eqp)/len(exist_eqp)*hash_rate[i][2]*1000*364.24*24*60*60/3600000000000000
        max_consumption = unprof_consumption
        min_consumption = unprof_consumption
        guess_consumption = unprof_consumption
        exist_eqp = []
    timestamp = prof_threshold[i][0]
    date = prof_threshold[i][1]
    try:
        c3.execute(insert_sql, (timestamp, date, max_consumption, min_consumption, guess_consumption))
    # If the row with this timestamp already exist, ignore it
    except sqlite3.IntegrityError:
        pass
    else:
        inserted_count += 1
    prof_eqp = []
    ### working with Energy D
            
#closing connections to DBs
conn.close()
conn2.close()
conn3.commit()
conn3.close()
