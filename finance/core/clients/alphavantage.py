###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-11-25
# Filename: alphavantage.py
# Description: Alpha Vantage client
###########################

import requests

from core.config.base import get_value as config_value


class AlphaVantage(object):
    """
    Alpha Vantage stock data client.
    """

    API_KEY = config_value('ALPHA_VANTAGE_API_KEY')

    URL = "https://www.alphavantage.co/query?function=" + \
        "TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=full&apikey={1}"

    def get_stock_data(self, ticker_symbol):
        """ (str) -> list of dict
        Returns stock data for the given ticker symbol.
        """
        response = requests.get(self.URL.format(ticker_symbol, self.API_KEY))
        return response.json()[config_value('ALPHA_VANTAGE_TIMESERIES_KEY')]
