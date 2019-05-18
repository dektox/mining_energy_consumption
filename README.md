# mining_energy_consumption
Calculation and visualization of energy consumed by Bitcoin mining

First run hash_rate_scrapper.py, it will create Data.db with the Difficulty, Hashrate, Price, and calculated Mining Profitability Threshold. Then run energy_calculation.py, it will calculate MIN, MAX, and GUESSED energy consumption rate and store it to Energy.db
OR you can make it crom:

15 * * * * cd /home/YOUR_PATH && $(which python3) hash_rate_scrapper.py --price 0.066 >> ~cron_hash.log 2>&1

16 * * * * cd /home/YOUR_PATH && $(which python3) energy_calculation.py >> ~cron_energy.log 2>&1

api folder contains chart_API.py creates web-server which returns data needed for Chart
You can make it run automatically by following the instructions https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

Index.html and server.js are to run the webpage 
