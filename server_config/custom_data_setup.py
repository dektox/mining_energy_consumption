# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:52:35 2019

@author: Anton
"""

import psycopg2
import yaml
import pandas as pd

config_path = '../CONFIG.yml'
if config_path:
    with open(config_path) as fp:
        config = yaml.load(fp, yaml.FullLoader)
else:
    config = {}

def empty_string_to_none(data):
    return list(map(lambda x: None if pd.isna(x) else x, data))
    
conn = psycopg2.connect(**config['custom_data'])
c = conn.cursor()

data = pd.read_csv("countries.csv")
country = list(data['country'])
code = list(data['code'])
electricity_consumption = list(data['electricity_consumption'])
country_flag = empty_string_to_none(list(data['country_flag']))
series_id = empty_string_to_none(list(data['series_id']))

data2 = pd.read_csv("miners.csv") 
miner_name = list(data2['Miner_name'])
unix_date_of_release = list(data2['UNIX_date_of_release'])
efficiency_j_gh = list(data2['Efficiency_J_Gh'])
qty = list(data2['Qty'])

c.execute("CREATE TABLE IF NOT EXISTS countries (country TEXT PRIMARY KEY, code TEXT, electricity_consumption REAL, country_flag TEXT, series_id TEXT, year INTEGER);")
c.execute("CREATE TABLE IF NOT EXISTS miners (miner_name TEXT PRIMARY KEY, unix_date_of_release INT, efficiency_j_gh REAL, qty INT);")
insert_sql = "INSERT INTO countries (country, code, electricity_consumption, country_flag, series_id) VALUES (%s, %s, %s, %s, %s);"
insert_sql2 = "INSERT INTO miners (miner_name, unix_date_of_release, efficiency_j_gh, qty) VALUES (%s, %s, %s, %s);"

for item in zip(country, code, electricity_consumption, country_flag, series_id):
    c.execute(insert_sql, item)
    
for item in zip(miner_name, unix_date_of_release, efficiency_j_gh, qty):
    c.execute(insert_sql2, item)

conn.commit()
conn.close()

# =============================================================================
# import csv
# from collections import defaultdict
# 
# columns = defaultdict(list) # each value in each column is appended to a list
# 
# with open('countries.csv') as f:
#     reader = csv.DictReader(f) # read rows into a dictionary format
#     for row in reader: # read a row as {column1: value1, column2: value2,...}
#         for (k,v) in row.items(): # go over each column name and value 
#             columns[k].append(v) # append the value into the appropriate list
#                                  # based on column name k
# 
# country=columns['country']
# code=columns['code']
# electricity_consumption=columns['electricity_consumption']
# country_flag=columns['country_flag']
# =============================================================================
