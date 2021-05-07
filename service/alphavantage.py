import arrow
import logging

from alpha_vantage.timeseries import TimeSeries
from generated.proto.config_pb2 import Config, Stock, DownloadConfig
from typing import Generator, List, Dict, Union

def download_data(config: Config) -> Generator[List[Dict[str, Union[str, int]]], None, None]:
    logging.info("Downloading stock history from Alphavantage.")
    counter = 0
    all_stocks = []
    for stock in config.stocks:
        if stock.api != Stock.Alphavantage:
            continue
        ts = TimeSeries()
        data, metadata = ts.get_daily_adjusted(
            symbol=stock.symbol,
            outputsize=DownloadConfig.AlphavantageOutputSize.Name(
                config.download_config.alphavantage_output_size,
            ),
        )

        number_of_tries = 0
        current_arrow_date = arrow.get(stock.first_transaction)
        while True:
            if counter == config.download_config.batch_size_for_persistence:
                yield all_stocks
                counter = 0
                all_stocks = []

            date_string = current_arrow_date.format(config.download_config.date_format)
            if number_of_tries > config.download_config.max_tries_before_end_of_trading:
                break

            if date_string not in data:
                number_of_tries += 1
                current_arrow_date = current_arrow_date.shift(days=1)
                continue

            stock_price = data[date_string]["5. adjusted close"]

            all_stocks.append({
                "ts": current_arrow_date.datetime.replace(tzinfo=None),
                "date": current_arrow_date.date(),
                "symbol": metadata["2. Symbol"],
                "price": float(stock_price),
            })
            counter += 1

            current_arrow_date = current_arrow_date.shift(days=1)
            number_of_tries = 0
    logging.info("Done downloading stock history from Alphavantage.")
    yield all_stocks
