import arrow
import pandas
import logging

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from generated.proto.config_pb2 import Config, Stock, DownloadConfig, OtherCurrencies
from typing import Generator, List, Dict, Union
from . import patch_missing_data

def download_data(config: Config) -> Generator[List[Dict[str, Union[str, int]]], None, None]:
    logging.info("Downloading stock history from Alphavantage.")
    for stock in config.stocks:
        all_stocks = []
        if stock.api != Stock.Alphavantage:
            continue
        ts = TimeSeries(output_format='pandas')
        df, _ = ts.get_daily_adjusted(
            symbol=stock.symbol,
            outputsize=DownloadConfig.AlphavantageOutputSize.Name(
                config.download_config.alphavantage_output_size,
            ),
        )
        df = df[df.index >= stock.first_transaction]
        df = patch_missing_data(df, stock)
        data_close_series = df["5. adjusted close"]
        data = data_close_series.to_dict()
        all_stocks = [
            {
                "ts": key.to_pydatetime().replace(tzinfo=None),
                "date": arrow.get(key.to_pydatetime()).format(config.download_config.date_format),
                "symbol": stock.symbol,
                "price": value,
                "currency": stock.currency,
            } for key, value in data.items()
        ]
        yield all_stocks
    logging.info("Done downloading stock history from Alphavantage.")


def download_foreign_exchange(config: Config) -> Generator[List[Dict[str, Union[str, int]]], None, None]:
    logging.info("Downloading fx history from Alphavantage.")
    for other_currency in config.currency.other_currencies:
        all_fx = []
        fx = ForeignExchange(output_format='pandas')
        df, _ = fx.get_currency_exchange_daily(
            from_symbol=other_currency.currency,
            to_symbol=config.currency.base_currency,
            outputsize=DownloadConfig.AlphavantageOutputSize.Name(
                config.download_config.alphavantage_output_size,
            ),
        )
        df[df.index >= other_currency.first_transaction]
        df = patch_missing_data(df, other_currency)
        data_close_series = df["4. close"]
        data = data_close_series.to_dict()
        all_fx = [
            {
                "ts": key.to_pydatetime().replace(tzinfo=None),
                "date": arrow.get(key.to_pydatetime()).format(config.download_config.date_format),
                "symbol": other_currency.currency,
                "price": value,
                "currency": config.currency.base_currency,
            } for key, value in data.items()
        ]
        yield all_fx
    logging.info("Done downloading fx history from Alphavantage.")
