###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-11-25
# Filename: alphavantage.py
# Description: Alpha Vantage client
###########################

import requests


class AlphaVantage(object):
    """
    Alpha Vantage stock data client.
    """

    API_KEY = "AST2ZP8MLEK9TJZS"    # Alpha Vantage stocks API

    URL = "https://www.alphavantage.co/query?function=" + \
        "TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=full&apikey={1}"

    def get_stock_data(self, ticker_symbol):
        """ (str) -> list of dict
        Returns stock data for the given ticker symbol.
        """
        response = requests.get(self.URL.format(ticker_symbol, self.API_KEY))
        timeseries_key = "Time Series (Daily)"
        return response.json()[timeseries_key]
