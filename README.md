# mining_energy_consumption
Calculation and visualization of energy consumed by Bitcoin mining

First run hash_rate_scrapper.py, it will create Data.db with the Difficulty, Hashrate, Price, and calculated Mining Profitability Threshold. 

Then run energy_calculation.py, it will calculate MIN, MAX, and GUESSED energy consumption rate and store it to Energy.db

chart_API.py creates web-server which returns data needed for Chart

Index.html and server.js are to run the page 
