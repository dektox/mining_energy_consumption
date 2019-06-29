# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:24:16 2019

@author: Anton
"""
from flask import Flask, jsonify
import flask
import requests
import time
from flask_cors import CORS
import psycopg2
import yaml

config_path = '../CONFIG.yml'
if config_path:
    with open(config_path) as fp:
        config = yaml.load(fp, yaml.FullLoader)
else:
    config = {}

def load_data():
    with psycopg2.connect(**config['blockchain_data']) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM prof_threshold')
        prof_threshold=c.fetchall()
        prof_threshold=prof_threshold[500:]   
        c.execute('SELECT * FROM hash_rate')
        hash_rate=c.fetchall()
        hash_rate=hash_rate[500:]
    with psycopg2.connect(**config['custom_data']) as conn2:   
        c2 = conn2.cursor()
        c2.execute('SELECT * FROM miners')
        miners=c2.fetchall()
        c2.execute('SELECT * FROM countries')
        countries=c2.fetchall()
    return prof_threshold, hash_rate, miners, countries

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
prof_threshold, hash_rate, miners, countries = load_data()
lastupdate = time.time()

@app.before_request
def before_request(): 
    global lastupdate, prof_threshold, hash_rate, miners, countries
    if time.time() - lastupdate > 3600:
        prof_threshold, hash_rate, miners, countries =load_data()
        lastupdate = time.time()
    
@app.route('/api/data/<value>')
def recalculate_data(value):
    
    price = float(value)
    k = 0.05/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
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
            max_consumption = max(prof_eqp)*hash_rate[i][2]*365.25*24/1e9
            min_consumption = min(prof_eqp)*hash_rate[i][2]*365.25*24/1e9
            guess_consumption = sum(prof_eqp)/len(prof_eqp)*hash_rate[i][2]*365.25*24/1e9
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
    return jsonify(data=response)


@app.route("/api/max/<value>")
def recalculate_max(value):
    
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    price = float(value)
    k = 0.05/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment

    for miner in miners:
        if prof_threshold[-1][0]>miner[1] and prof_threshold[-1][2]*k>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    try:
        max_consumption = max(prof_eqp)*hashrate*1.2/1e9
    except:
        max_consumption = 'mining is not profitable'
    return jsonify(max_consumption)


@app.route("/api/min/<value>")
def recalculate_min(value):
    
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    price = float(value)
    k = 0.05/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment

    for miner in miners:
        if prof_threshold[-1][0]>miner[1] and prof_threshold[-1][2]*k>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    try:
        min_consumption = min(prof_eqp)*hashrate*1.01/1e9
    except:
        min_consumption = 'mining is not profitable'
    return jsonify(min_consumption)


@app.route("/api/guess/<value>")
def recalculate_guess(value):
    
    hashrate = requests.get("https://blockchain.info/q/hashrate").json()
    price = float(value)
    k = 0.05/price # that is because basee calculations in the DB is for the price 0.066 USD/KWth
    
    prof_eqp = []   # temprorary var for the list of profitable equipment efficiency at any given moment

    for miner in miners:
        if prof_threshold[-1][0]>miner[1] and prof_threshold[-1][2]*k>miner[2]: prof_eqp.append(miner[2])
        # ^^current date and date of miner release ^^checks if miner is profitable ^^if yes, adds miner's efficiency to the list
    try:
        guess_consumption = sum(prof_eqp)/len(prof_eqp)*hashrate*1.10/1e9
    except:
        guess_consumption = 'mining is not profitable'
    return jsonify(guess_consumption)

# =============================================================================
# @app.route("/api/countries", methods=['GET','POST'])
# def countries_old():
#     jsonify(data=countries)
# =============================================================================

@app.route("/api/countries", methods=['GET','POST'])
def countries_btc():
    
     prof_eqp = all_prof_eqp = guess_consumption_all = []
     for i in range(0, len(prof_threshold)):
         for miner in miners:
             if (prof_threshold[i][0]>miner[1] and prof_threshold[i][2]>miner[2]): prof_eqp.append(miner[2])
         all_prof_eqp.append(prof_eqp)
         try:
             guess_consumption = sum(prof_eqp)/len(prof_eqp)*hash_rate[i][2]*365.25*24*1.10/1e9
         except: #in case if mining is not profitable (it is impossible to find MIN or MAX of empty list)
             guess_consumption = guess_consumption_all[-1]
         guess_consumption_all.append(guess_consumption)
         prof_eqp = []  
         
     local = countries
     local.append(('Bitcoin','BTC',round(guess_consumption_all[-1],2),'data:image/png;base64,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'))
     def takeThird(elem):
         return elem[2]
     local = sorted(local, key=takeThird, reverse=True)
     local=list(enumerate(local,1))
     response = []
     for item in local:
         response.append({
            'x': item[1][0],
            'y': item[1][2],        
            'country_rank': item[0], 
            'bitcoin_percentage': round(item[1][2]/guess_consumption_all[-1]*100,2),
            'logo': item[1][3]
            })
     return jsonify(response)

@app.route("/api/feedback", methods=['POST'])
def feedback():
    content = flask.request.json
    with psycopg2.connect(**config['custom_data']) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS feedback (timestamp INT," 
                  "name TEXT, organisation TEXT, email TEXT, message TEXT);")
        insert_sql = "INSERT INTO feedback (timestamp, name, organisation, email, message) VALUES (%s, %s, %s, %s, %s)"
        name = content['name']
        organisation = content['organisation']
        email = content['email']
        message = content['message']
        timestamp = int(time.time())
        try:
            c.execute(insert_sql, (timestamp, name, organisation, email, message))
        except Exception as error:
            return jsonify(data=content,status="fail",error=error.pgcode)
    return jsonify(data=content,status="success",error="")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', use_reloader=True)  
