from core.clients.alphavantage import AlphaVantage
from datetime import date, datetime, timedelta


class StocksService(object):

    def __init__(self):
        self.data_client = AlphaVantage()

    def one_day_ago(self, dt=None, n=1):
        if dt is None:
            dt = datetime.today()
        return dt - timedelta(days=n)

    def one_year_ago_date(self):
        result = datetime.today()
        try:
            result = result.replace(year=result.year - 1)
        except ValueError:
            result = result + (date(result.year - 1, 1, 1) -
                               date(result.year, 1, 1))
        return result

    def date_to_string(self, dt):
        return dt.strftime('%Y-%m-%d')

    def timeseries_lookup(self, timeseries, dt):
        """
        Return the day summary for day `dt` in the stock data from
        the given `timeseries`. Includes retry logic for the closest
        day within the past 2 years. Raises `Exception` if no data could
        be found with these parameters.
        """
        if dt in timeseries:
            return timeseries[self.date_to_string(dt)]

        # Retry logic
        while not self.date_to_string(dt) in timeseries and \
                datetime.today().year - dt.year <= 2:
            dt = self.one_day_ago(dt)
        if self.date_to_string(dt) in timeseries:
            return timeseries[self.date_to_string(dt)]

        raise Exception('Error: No timeseries data for {}.'.format(dt))

    def extract_adjusted_close(self, day_summary):
        return float(day_summary['5. adjusted close'])

    def get_performance(self, ticker_symbol):
        timeseries = self.data_client.get_stock_data(ticker_symbol)

        old_ts_entry = self.timeseries_lookup(
            timeseries, self.one_year_ago_date())
        new_ts_entry = self.timeseries_lookup(timeseries, self.one_day_ago())

        old_adjusted_close = self.extract_adjusted_close(old_ts_entry)
        new_adjusted_close = self.extract_adjusted_close(new_ts_entry)

        return 100 * ((new_adjusted_close / old_adjusted_close) - 1)
