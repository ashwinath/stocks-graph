import arrow

from alpha_vantage.timeseries import TimeSeries

DATE_FORMAT = "YYYY-MM-DD"

FIRST_TRANSACTION = "2021-03-11"
MAX_TRIES = 30 # there shouldnt be more than 30 non trading days at once

if __name__ == "__main__":
    ts = TimeSeries()
    data, metadata = ts.get_daily_adjusted(symbol="IWDA.LON", outputsize="full")

    all_stocks = []
    number_of_tries = 0
    current_arrow_date = arrow.get(FIRST_TRANSACTION)
    while True:
        date_string = current_arrow_date.format(DATE_FORMAT)
        if number_of_tries > MAX_TRIES:
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

    import pprint
    pprint.pprint(all_stocks)
