# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:24:16 2019

@author: Anton
"""

from flask import Flask, jsonify
import sqlite3
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/api/data", methods=['GET','POST'])
def chart_API():
     
    conn = sqlite3.connect('../energy.db', timeout=3)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute('SELECT timestamp, date, max_consumption, min_consumption, guess_consumption FROM energy_consumption')
    energy_consumption=c.fetchall()
    conn.close()
    return jsonify(data=energy_consumption)    

@app.route("/api/guess", methods=['GET','POST'])
def guess_API():
     
    conn = sqlite3.connect('../energy.db', timeout=2)
    c = conn.cursor()
    c.execute('SELECT all_prof_eqp FROM energy_consumption')
    all_prof_eqp=c.fetchall()
    conn.close()
    prof_eqp = list(map(float, all_prof_eqp[-1][0].split(','))) #converting string to list of floats
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    guess = sum(prof_eqp)/len(prof_eqp)*hashrate*365.25*24*60*60/3600000000000000
    guess_str = str(guess)
    return guess_str    

@app.route("/api/max", methods=['GET','POST'])
def max_API():
     
    conn = sqlite3.connect('../energy.db', timeout=1)
    c = conn.cursor()
    c.execute('SELECT all_prof_eqp FROM energy_consumption')
    all_prof_eqp=c.fetchall()
    conn.close()
    prof_eqp = list(map(float, all_prof_eqp[-1][0].split(','))) #converting string to list of floats
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    MAX = max(prof_eqp)*hashrate*365.25*24*60*60/3600000000000000
    MAX_str = str(MAX)
    return MAX_str    

@app.route("/api/min", methods=['GET','POST'])
def min_API():
     
    conn = sqlite3.connect('../energy.db', timeout=1)
    c = conn.cursor()
    c.execute('SELECT all_prof_eqp FROM energy_consumption')
    all_prof_eqp=c.fetchall()
    conn.close()
    prof_eqp = list(map(float, all_prof_eqp[-1][0].split(','))) #converting string to list of floats
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    MIN = min(prof_eqp)*hashrate*365.25*24*60*60/3600000000000000
    MIN_str = str(MIN)
    return MIN_str

@app.route('/api/data/<value>')
def recalculate_data(value):
    conn = sqlite3.connect('../data.db')
    conn2 = sqlite3.connect('../miners.db')
    c = conn.cursor()
    c2 = conn2.cursor()
    c.execute('SELECT * FROM prof_threshold')
    prof_threshold=c.fetchall()
    c.execute('SELECT * FROM hash_rate')
    hash_rate=c.fetchall()
    c2.execute('SELECT * FROM miners')
    miners=c2.fetchall()
    
    price = float(value)
    k = 0.066/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment
    exist_eqp = []  # temprorary var for the list of existing equipment efficiency at moment when mining is not profitable
    all_prof_eqp = []  # list of lists of profitable equipment efficiency in all the dates
    all_exist_eqp = [] 
    max_consumption_all = []
    min_consumption_all = []
    guess_consumption_all = []
    response = []

    for i in range(0, len(prof_threshold)):
        for miner in miners:
            if prof_threshold[i][0]>miner[1] and prof_threshold[i][2]*k>miner[2]: prof_eqp.append(miner[2])
            # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
        all_prof_eqp.append(prof_eqp)
        try:
            max_consumption = max(prof_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000
            min_consumption = min(prof_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000
            guess_consumption = sum(prof_eqp)/len(prof_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000    
        except: #in case if mining is not profitable (it is impossible to find MIN or MAX of empty list)
            for miner in miners:
                if prof_threshold[i][0]>miner[1]: exist_eqp.append(miner[2])
            all_exist_eqp.append(exist_eqp)
            unprof_consumption = sum(exist_eqp)/len(exist_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000
            max_consumption = unprof_consumption
            min_consumption = unprof_consumption
            guess_consumption = unprof_consumption
            exist_eqp = []
        max_consumption_all.append(max_consumption)
        min_consumption_all.append(min_consumption)
        guess_consumption_all.append(guess_consumption)
        timestamp = prof_threshold[i][0]
        date = prof_threshold[i][1]
        response.append({
                'date': date,
                'guess_consumption': guess_consumption,
                'max_consumption': max_consumption, 
                'min_consumption': min_consumption, 
                'timestamp': timestamp,
                })
    conn.close()
    conn2.close()
    return jsonify(data=response)


@app.route("/api/max/<value>")
def recalculate_max(value):

    conn = sqlite3.connect('../data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prof_threshold')
    prof_threshold=c.fetchall()
    conn2 = sqlite3.connect('../miners.db')
    c2 = conn2.cursor()
    c2.execute('SELECT * FROM miners')
    miners=c2.fetchall()
    conn.close()
    conn2.close()
    
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    price = float(value)
    k = 0.066/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment

    for miner in miners:
        if prof_threshold[-1][0]>miner[1] and prof_threshold[-1][2]*k>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    try:
        max_consumption = max(prof_eqp)*hashrate*1000*365.25*24*60*60/3600000000000000
    except:
        max_consumption = 'mining is not profitable'
    return jsonify(max_consumption)


@app.route("/api/min/<value>")
def recalculate_min(value):

    conn = sqlite3.connect('../data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prof_threshold')
    prof_threshold=c.fetchall()
    conn2 = sqlite3.connect('../miners.db')
    c2 = conn2.cursor()
    c2.execute('SELECT * FROM miners')
    miners=c2.fetchall()
    conn.close()
    conn2.close()
    
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    price = float(value)
    k = 0.066/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment

    for miner in miners:
        if prof_threshold[-1][0]>miner[1] and prof_threshold[-1][2]*k>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    try:
        min_consumption = min(prof_eqp)*hashrate*1000*365.25*24*60*60/3600000000000000
    except:
        min_consumption = 'mining is not profitable'
    return jsonify(min_consumption)


@app.route("/api/guess/<value>")
def recalculate_guess(value):

    conn = sqlite3.connect('../data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prof_threshold')
    prof_threshold=c.fetchall()
    conn2 = sqlite3.connect('../miners.db')
    c2 = conn2.cursor()
    c2.execute('SELECT * FROM miners')
    miners=c2.fetchall()
    conn.close()
    conn2.close()
    
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    price = float(value)
    k = 0.066/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment

    for miner in miners:
        if prof_threshold[-1][0]>miner[1] and prof_threshold[-1][2]*k>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    try:
        guess_consumption = sum(prof_eqp)/len(prof_eqp)*hashrate*1000*365.25*24*60*60/3600000000000000
    except:
        guess_consumption = 'mining is not profitable'
    return jsonify(guess_consumption)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', use_reloader=True)  