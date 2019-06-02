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

@app.route('/api/data/<value>')
def recalculate_data(value):
    conn = sqlite3.connect('../data.db')
    conn2 = sqlite3.connect('../miners.db')
    c = conn.cursor()
    c2 = conn2.cursor()
    c.execute('SELECT * FROM prof_threshold')
    prof_threshold=c.fetchall()
    prof_threshold=prof_threshold[500:-1]    
    c.execute('SELECT * FROM hash_rate')
    hash_rate=c.fetchall()
    hash_rate=hash_rate[500:-1]
    c2.execute('SELECT * FROM miners')
    miners=c2.fetchall()
    
    price = float(value)
    k = 0.066/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment
    all_prof_eqp = []  # list of lists of profitable equipment efficiency in all the dates
    max_consumption_all = []
    min_consumption_all = []
    guess_consumption_all = []
    response = []

    for i in range(0, len(prof_threshold)):
        for miner in miners:
            if (prof_threshold[i][0]>miner[1] and prof_threshold[i][2]*k>miner[2]): prof_eqp.append(miner[2])
            # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
        all_prof_eqp.append(prof_eqp)
        try:
            max_consumption = max(prof_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000
            min_consumption = min(prof_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000
            guess_consumption = sum(prof_eqp)/len(prof_eqp)*hash_rate[i][2]*1000*365.25*24*60*60/3600000000000000
        except: #in case if mining is not profitable (it is impossible to find MIN or MAX of empty list)
            max_consumption = max_consumption_all[-1]
            min_consumption = min_consumption_all[-1]
            guess_consumption = guess_consumption_all[-1]
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
        prof_eqp = []
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
        max_consumption = max(prof_eqp)*hashrate*365.25*24*60*60/3600000000000000
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
        min_consumption = min(prof_eqp)*hashrate*365.25*24*60*60/3600000000000000
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
        guess_consumption = sum(prof_eqp)/len(prof_eqp)*hashrate*365.25*24*60*60/3600000000000000
    except:
        guess_consumption = 'mining is not profitable'
    return jsonify(guess_consumption)

@app.route("/api/countries", methods=['GET','POST'])
def countries():
     
    conn = sqlite3.connect('../countries.db', timeout=1)
    c3 = conn.cursor()
    c3.execute('SELECT * FROM countries')
    countries=c3.fetchall()
    conn.close()
    return jsonify(data=countries)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', use_reloader=True)  
