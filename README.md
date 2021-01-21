# mining_energy_consumption
Calculation and visualization of energy consumed by Bitcoin mining

First run hash_rate_scrapper.py, it will create Data.db with the Difficulty, Hashrate, Price, Miners_profirs and calculated Mining Profitability Threshold for default price. Then run energy_calculation.py, it will calculate MIN, MAX, and GUESSED energy consumption rate and store it to Energy.db
OR you can make it cron:

> 15 * * * * cd /home/YOUR_PATH && $(which python3) hash_rate_scrapper.py --price 0.05 >> ~cron_hash.log 2>&1
> 16 * * * * cd /home/YOUR_PATH && $(which python3) energy_calculation.py >> ~cron_energy.log 2>&1

/api folder contains chart_API.py which is Flask app for API. 
Default port is 127.0.0.1/api/{endpoint}/{your_price_guess}
Endpoints: data [for chart], min, max, guess

You can make it run automatically by following the instructions https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04 (don't forget to install additional libraries in venv)

If something changes to frontend, make first
> git pull

then in the /frontend directory execute 
> npm run build

To run jenkins ufter reload
> cd /home/ci/jenkins
> docker-compose up -d

To run pm2 after reload
> pm2 start pm2.config.js
