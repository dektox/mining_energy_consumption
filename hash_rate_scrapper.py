import logging
import sqlite3
from datetime import datetime
from pprint import pformat

import requests
import click

DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_DATABASE_FILE = 'data.db'
DEFAULT_ELECTRICITY_PRICE = 0.05

LOGGER = logging.getLogger()


def crawl(endpoint):
    # Showing message that the scrapping started
    LOGGER.info(f"{endpoint}: Scrapping for {datetime.utcnow().isoformat()}")
    # Querying data from DATA_API_URL
    resp = requests.get(f"https://api.blockchain.info/charts/{endpoint}?timespan=6years")
    # Transforming reply into the object of 'dict' type
    data = resp.json()
    LOGGER.debug(f"{endpoint}: Response:\n\n{pformat(data)}\n\n")
    return [(int(row['x']), row['y']) for row in data['values']]

crawl('hash-rate')

def save_values(values, connection, table_name):
    # Creating cursor to work with DB
    cursor = connection.cursor()
    # Creating table. timestamp is a PRIMARY KEY, values are unique
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}"
                   f" (timestamp INT PRIMARY KEY, date TEXT, value REAL);")

    inserted_count = 0
    # Template of the query to paste a row to a table
    insert_sql = f"INSERT INTO {table_name} ('timestamp', 'date', 'value') VALUES (?, ?, ?);"
    # Taking 'values' from the API reply and inputting rows one by one
    for timestamp, value in values:
        # The second column is going to be date in readable format
        date = datetime.utcfromtimestamp(timestamp).isoformat()
        # Trying to insert row
        try:
            cursor.execute(insert_sql, (timestamp, date, value))
        # If the row with this timestamp already exist, ignore it
        except sqlite3.IntegrityError:
            pass
        else:
            inserted_count += 1
    LOGGER.info(f"{table_name}: Saved {inserted_count} new values")

# this is to have posibility to change parameters such as electricity price from a command line
@click.command()
@click.option('--database', '-d', default=DEFAULT_DATABASE_FILE)
@click.option('--price', '-p', default=DEFAULT_ELECTRICITY_PRICE)
@click.option('--log-level', '-l', default=DEFAULT_LOG_LEVEL)
def main(database, log_level, price):
    # Logging
    LOGGER.setLevel(log_level.upper())
    # Console outputs
    LOGGER.addHandler(logging.StreamHandler())

    all_data = {}
    # Opening DB. When the 'with' block ends, connection will be closed
    with sqlite3.connect(database) as connection:
        for endpoint in ['difficulty', 'hash-rate', 'market-price']: #if you need more data, just list it here
            values = crawl(endpoint)
            table_name = endpoint.replace('-', '_') #this is because table name can't contain hyphens
            save_values(values, connection, table_name)
            for timestamp, value in values:
                try:
                    all_data[timestamp][endpoint] = value
                except KeyError:
                    all_data[timestamp] = {endpoint: value}

        # This is to create block reward time series
        for timestamp, data in all_data.items():
            # 0 <= timestamp < 28 November 2012
            if timestamp < 1353967200:
                data['block-reward'] = 50.0
            # 28 November 2012 <= timestamp < 9 July 2016
            elif timestamp < 1467925200:
                data['block-reward'] = 25.0
            # 9 July 2016 <= timestamp < 01 May 2020   #this is fishy :-)
            elif timestamp < 1588291200:
                data['block-reward'] = 12.5
            else:
                LOGGER.warning(f"Timestamp {timestamp} is out of range. Cannot assign a block reward value")
                data['block-reward'] = None
        save_values(((timestamp, data['block-reward']) for timestamp, data in all_data.items()),
                    connection, 'block_reward')

        # Progitability threshold calculation
        for timestamp, data in all_data.items():
            try:
                data['prof-threshold'] = 1.0e+09 / (2 ** 32 * data['difficulty']) * data['block-reward']\
                                             * data['market-price'] / price * 3.6e+06
            except KeyError:
                pass
            except ZeroDivisionError:
                data['prof-threshold'] = float('inf')
                LOGGER.warning(f"Zero division error: timestamp={timestamp}, data={data}")
        save_values(((timestamp, data['prof-threshold']) for timestamp, data
                     in all_data.items() if 'prof-threshold' in data),
                    connection, 'prof_threshold')    

if __name__ == '__main__':
    main()
