import arrow
from alpha_vantage.timeseries import TimeSeries

def download_data(config):
    data = {}
    for stock in config.stocks:
        ts = TimeSeries()
        data, metadata = ts.get_daily_adjusted(
            symbol=stock.symbol,
            outputsize=config.download_config.output_size,
        )

        all_stocks = []
        number_of_tries = 0
        current_arrow_date = arrow.get(stock.first_transaction)
        while True:
            date_string = current_arrow_date.format(config.download_config.date_format)
            if number_of_tries > config.download_config.max_tries_before_end_of_trading:
                break

            if date_string not in data:
                number_of_tries += 1
                current_arrow_date = current_arrow_date.shift(days=1)
                continue

            stock_price = data[date_string]["5. adjusted close"]
            all_stocks.append({
                "date": current_arrow_date.datetime,
                "price": stock_price,
                "symbol": metadata["2. Symbol"],
            })

            current_arrow_date = current_arrow_date.shift(days=1)
            number_of_tries = 0

        data["stock.symbol"] = all_stocks

    return data
