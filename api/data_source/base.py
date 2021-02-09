from enum import Enum, auto


class Values(Enum):
    def _generate_next_value_(name, start, count, last_values) -> str:
        return name.lower().replace('_', '-')

    MARKET_PRICE = auto()
    DIFFICULTY = auto()
    HASH_RATE = auto()
    MINERS_REVENUE = auto()


class DataSource:

    def __init__(self, url, assets='btc'):
        self.base_url = url
        self.assets = assets

    def get_values(self, *args, **kwargs):
        raise NotImplementedError
