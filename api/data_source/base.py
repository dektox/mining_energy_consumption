from datetime import datetime
from enum import Enum, auto


class Values(Enum):
    def _generate_next_value_(name, start, count, last_values) -> str:
        return name.lower().replace('_', '-')

    MARKET_PRICE = auto()
    DIFFICULTY = auto()
    HASH_RATE = auto()
    MINERS_REVENUE = auto()


class DataSource:

    def __init__(self, url, assets='btc', start_date='2014-05-28'):
        self.base_url = url
        self.assets = assets
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')

    def get_values(self, *args, **kwargs):
        raise NotImplementedError
