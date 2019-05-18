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
    guess = sum(prof_eqp)/len(prof_eqp)*hashrate*364.24*24*60*60/3600000000000000
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
    MAX = max(prof_eqp)*hashrate*364.24*24*60*60/3600000000000000
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
    MIN = min(prof_eqp)*hashrate*364.24*24*60*60/3600000000000000
    MIN_str = str(MIN)
    return MIN_str    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', use_reloader=True)  