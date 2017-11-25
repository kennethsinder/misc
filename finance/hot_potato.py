#!/usr/bin/env python
###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-09-29
# Filename: hot_potato.py
# Description: Determines best ETF investment for Hot Potato strategy
#       http://www.moneysense.ca/save/investing/celebrating-the-hot-potato/
###########################

# Disclaimers:
# - this was just for fun. I am not an investment professional.
# - please do not use the API key in alphavantage.py

from core.services.stocks import StocksService

# Change TICKERS to the desired index portfolio
TICKERS = {"Canadian equities": "VCN.TO", "US equities": "VUN.TO",
           "International equities": "XEF.TO", "Canadian bonds": "VAB.TO"}

service = StocksService()


def format_performance(ticker_symbol, performance, name=None):
    if name is None:
        message = '{} performance over the last year: {:0.2f}%'
        return message.format(ticker_symbol, performance)
    message = '{} ({}) performance over the last year: {:0.2f}%'
    return message.format(name, ticker_symbol, performance)


def perform_tour():
    """ () -> None
    Prints messages indicating the highest-performing ETF or stock
    from the values of `TICKERS`, over the last year, approximately.
    """
    ticker_performance = []
    for ticker_name in TICKERS:
        ticker_symbol = TICKERS[ticker_name]
        performance = service.get_performance(ticker_symbol)
        print(format_performance(ticker_symbol, performance, ticker_name))
        ticker_performance.append((ticker_symbol, ticker_name, performance))
    max_performance = max(ticker_performance, key=lambda t: t[2])
    print('Choose: {} ({}), with annual {:0.2f}%'.format(max_performance[1],
                                                         max_performance[0], max_performance[2]))


if __name__ == "__main__":
    perform_tour()
