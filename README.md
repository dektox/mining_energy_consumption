# mining_energy_consumption
Calculation and visualization of energy consumed by Bitcoin mining

First run custom_data_setup.py in /server_config to create DB and populate it with the countries and mining machines

Then run data_fetch_calc.py, it will calculate MIN, MAX, and GUESSED energy consumption rate and store it to the DB
OR you can make it cron:

> 51 * * * *  /usr/bin/python3 /home/cbeci/mining_energy_consumption/data_fetch_calc.py >>  /home/cbeci/mining_energy_consumption/scraper.log 2>&1

/api folder contains chart_API.py which is Flask app for API. 
Default port is 127.0.0.1/api/{endpoint}/{your_price_guess}
Endpoints: data [for chart], min, max, guess

You can make it run automatically by following the instructions https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04 (don't forget to install additional libraries in venv)

If something changes to frontend, make first
> git pull

then in the /frontend directory execute 
> npm run build

To run jenkins after reload
> cd /home/ci/jenkins
> docker-compose up -d

To run pm2 after reload
> pm2 start pm2.config.js
