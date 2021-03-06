import requests
import logging
from datetime import datetime
import dateutil.parser
from pprint import pformat
from typing import List
from urllib.parse import urljoin
from .base import DataSource, Values

LOGGER = logging.getLogger()


class CoinMetrics(DataSource):

    def __init__(self, url='https://community-api.coinmetrics.io/v4/', assets='btc', start_date='2014-05-28'):
        super().__init__(url=url, assets=assets, start_date=start_date)

    @staticmethod
    def _to_item(values) -> dict:
        item = {
            'timestamp': dateutil.parser.parse(values['time']).timestamp(),
            'asset': values['asset'],
            'difficulty': None,
            'hash-rate': None,
            'market-price': None,
            'miners-revenue': None,
        }

        if 'DiffMean' in values and values['DiffMean'] is not None:
            item['difficulty'] = float(values['DiffMean'])
        if 'HashRate' in values and values['HashRate'] is not None:
            item['hash-rate'] = float(values['HashRate'])
        if 'PriceUSD' in values and values['PriceUSD'] is not None:
            item['market-price'] = float(values['PriceUSD'])
        if all(value in values and values[value] is not None for value in ('IssTotUSD', 'FeeTotUSD')):
            item['miners-revenue'] = float(values['IssTotUSD']) + float(values['FeeTotUSD'])

        return item

    def get_values(self, values=None, assets=None, start_date=None) -> List[dict]:
        metrics_data = self.get_metrics_data(values=values, assets=assets, start_date=start_date)

        return [self._to_item(values) for values in metrics_data['data']]

    def get_metrics_data(self, values=None, start_date=None, assets=None) -> dict:
        if assets is None:
            assets = self.assets
        if values is None:
            values = list(Values)
        if start_date is not None:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        elif start_date is None and self.start_date is not None:
            start_date = self.start_date

        # Choosing the requested metrics
        metrics = []
        if Values.MARKET_PRICE in values:
            metrics.append('PriceUSD')
        if Values.DIFFICULTY in values:
            metrics.append('DiffMean')
        if Values.HASH_RATE in values:
            metrics.append('HashRate')
        if Values.MINERS_REVENUE in values:
            metrics.extend(['IssTotUSD', 'FeeTotUSD'])

        # request payload
        # see https://docs.coinmetrics.io/api/v4/#operation/getTimeseriesAssetMetrics
        params = {
            # Comma separated list of assets
            'assets': assets,
            # Comma separated metrics to request time series data for
            'metrics': ",".join(metrics),
            # Number of items per single page of results
            'page_size': 10000,
        }
        if start_date:
            # Start of the time interval in ISO 8601 format
            params['start_time'] = start_date.isoformat()

        metrics_str = ', '.join(value.value for value in values)
        LOGGER.info(f"{metrics_str}: Scrapping as of {datetime.utcnow().isoformat()}")
        
        # sending request to api and get json response
        response = requests.get(
            urljoin(self.base_url, 'timeseries/asset-metrics'), params=params
        ).json()

        LOGGER.debug(f"{metrics_str}: Response:\n\n{pformat(response)}\n\n")

        return response
