import requests
from datetime import datetime
import dateutil.parser
from typing import List
from urllib.parse import urljoin
from .base import DataSource, Values


class CoinMetrics(DataSource):

    def __init__(self, url='https://community-api.coinmetrics.io/v4/', assets='btc'):
        super().__init__(url, assets)
        self.start_date = None

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

    def get_values(self, values=None, assets=None) -> List[dict]:
        metrics_values = self.get_metrics_values(values=values, assets=assets)

        return [self._to_item(values) for values in metrics_values['data']]

    def get_metrics_values(self, values=None, start_date=None, assets=None) -> dict:
        if assets is None:
            assets = self.assets
        if values is None:
            values = list(Values)
        if start_date is None and self.start_date is not None:
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
            params['start_time'] = datetime.strptime(start_date, '%Y-%m-%d').isoformat()

        # sending request to api and get json response
        return requests.get(
            urljoin(self.base_url, 'timeseries/asset-metrics'), params=params
        ).json()
