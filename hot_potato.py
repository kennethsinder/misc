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
# - please do not use the below API key

import requests
from datetime import date, datetime, timedelta

# Change TICKERS to the desired index portfolio
TICKERS = {"Canadian equities": "VCN.TO", "US equities": "VUN.TO", \
    "International equities": "XEF.TO", "Canadian bonds": "VAB.TO"}

API_KEY = "AST2ZP8MLEK9TJZS"    # Alpha Vantage stocks API

URL = "https://www.alphavantage.co/query?function=" + \
    "TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=full&apikey={1}"

def get_stock_data(ticker_symbol):
    response = requests.get(URL.format(ticker_symbol, API_KEY))
    timeseries_key = "Time Series (Daily)"
    return response.json()[timeseries_key]

def one_day_ago(dt=None, n=1):
    if dt is None:
        dt = datetime.today()
    return dt - timedelta(days=n)

def one_year_ago_date():
    result = datetime.today()
    try:
        result = result.replace(year=result.year-1)
    except ValueError:
        result = result + (date(result.year - 1, 1, 1) - date(result.year, 1, 1))
    return result

def date_to_string(dt):
    return dt.strftime('%Y-%m-%d')

def timeseries_lookup(timeseries, dt):
    if dt in timeseries:
        return timeseries[date_to_string(dt)]

    # Retry logic
    while not date_to_string(dt) in timeseries and \
            datetime.today().year - dt.year <= 2:
        dt = one_day_ago(dt)
    if date_to_string(dt) in timeseries:
        return timeseries[date_to_string(dt)]

    print("FATAL ERROR: No timeseries data for one year ago.")
    quit()

def extract_adjusted_close(day_summary):
    return float(day_summary['5. adjusted close'])

def get_performance(ticker_symbol):
    timeseries = get_stock_data(ticker_symbol)

    old_ts_entry = timeseries_lookup(timeseries, one_year_ago_date())
    new_ts_entry = timeseries_lookup(timeseries, one_day_ago())

    old_adjusted_close = extract_adjusted_close(old_ts_entry)
    new_adjusted_close = extract_adjusted_close(new_ts_entry)

    return 100 * ((new_adjusted_close / old_adjusted_close) - 1)

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
        performance = get_performance(ticker_symbol)
        print(format_performance(ticker_symbol, performance, ticker_name))
        ticker_performance.append((ticker_symbol, ticker_name, performance))
    max_performance = max(ticker_performance, key=lambda t: t[2])
    print('Choose: {} ({}), with annual {:0.2f}%'.format(max_performance[1], \
        max_performance[0], max_performance[2]))

if __name__ == "__main__":
    perform_tour()
