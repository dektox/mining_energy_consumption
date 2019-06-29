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
    
     prof_eqp = guess_consumption = guess_consumption_all = []
     for i in range(0, len(prof_threshold)):
         for miner in miners:
             if (prof_threshold[i][0]>miner[1] and prof_threshold[i][2]>miner[2]): prof_eqp.append(miner[2])
         try:
             guess_consumption = sum(prof_eqp)/len(prof_eqp)*hash_rate[i][2]*365.25*24*1.10/1e9
         except: #in case if mining is not profitable (it is impossible to find MIN or MAX of empty list)
             guess_consumption = guess_consumption_all[-1]
         guess_consumption_all.append(guess_consumption)
         prof_eqp = []  
      
     tup2dict = {a:[c,d] for a,b,c,d in countries}
     tup2dict['Bitcoin'][0] = float(guess_consumption_all[-1])
     dictsort=sorted(tup2dict.items(), key = lambda i: i[1][0], reverse=True)
# =============================================================================
#      def takeThird(elem):
#          return elem[2]
#      local = sorted(local, key=takeThird, reverse=True)
#      local = list(enumerate(local,1))
# =============================================================================
     response = []
     for item in dictsort:
         response.append({
            'country': item[0],
            'y': item[1][0],        
            'x': dictsort.index(item)+1,
            'bitcoin_percentage': round(item[1][0]/guess_consumption_all[-1]*100,2),
            'logo': item[1][1]
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
