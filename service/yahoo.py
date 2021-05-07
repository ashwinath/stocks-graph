import arrow
import logging
import yfinance as yf

from generated.proto.config_pb2 import Config, Stock, DownloadConfig
from typing import Generator, List, Dict, Union

def download_data(config: Config) -> Generator[List[Dict[str, Union[str, int]]], None, None]:
    logging.info("Downloading stock history from Yahoo.")
    counter = 0
    for stock in config.stocks:
        all_stocks = []
        if stock.api != Stock.Yahoo:
            continue
        ticker = yf.Ticker(stock.symbol)
        history_df = ticker.history(
            period=DownloadConfig.YahooPeriod.Name(config.download_config.yahoo_period),
            interval="1d",
        )
        history_df = history_df[history_df.index >= stock.first_transaction]
        date_close_series = history_df["Close"]
        data = date_close_series.to_dict()
        all_stocks = [
            {
                "ts": key.to_pydatetime().replace(tzinfo=None),
                "date": arrow.get(key.to_pydatetime()).format(config.download_config.date_format),
                "symbol": stock.symbol,
                "price": value,
            } for key, value in data.items()
        ]

        logging.info("Done downloading stock history from Yahoo.")
        yield all_stocks
