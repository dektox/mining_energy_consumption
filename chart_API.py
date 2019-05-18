# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:24:16 2019

@author: Anton
"""

from flask import Flask
import json
import sqlite3
app = Flask(__name__)
app.config["DEBUG"] = True

#connecting to DBs, downloading data
conn = sqlite3.connect('energy.db')
c = conn.cursor()

c.execute('SELECT * FROM energy_consumption')
energy_consumption=c.fetchall()
rs = json.dumps(energy_consumption)

@app.route("/", methods=['GET'])
def hello():
    return rs

if __name__ == '__main__':
    app.run(host = "134.209.182.57")