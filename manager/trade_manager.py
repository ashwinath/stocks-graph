import arrow
import logging

from generated.proto.trades_pb2 import TradeHistory, Trade
from typing import List
from . import Manager

DATE_STRATEGY_FORWARD = "forward"
DATE_STRATEGY_BACKWARD = "backward"

class TradeManager(Manager):
    def process(self, trades: List[TradeHistory]):
        logging.info("Processing trades")
        for one_batch in trades:
            self._process_batch(one_batch)
        logging.info("Done processing trades")

    def _process_batch(self, trade_batch: TradeHistory):
        data = []
        for trade in trade_batch.trades:
            logging.info(f"Processing trade: {trade.symbol}, date: {trade.date}")
            ts = arrow.get(trade.date).datetime.replace(tzinfo=None)
            total_in_base_currency = self._calculate_base_currency(trade)
            if trade.type == Trade.sell:
                trade.quantity *= -1

            trade_model = {
                "ts": ts,
                "date": trade.date,
                "symbol": trade.symbol,
                "price_each": trade.price_each,
                "quantity": trade.quantity,
                "currency": trade.currency,
                "total_in_base_currency": total_in_base_currency,
            }
            data.append(trade_model)
        self._db.save_trades(data)

    def _calculate_base_currency(self, trade: Trade):
        total_in_base_currency = trade.quantity * trade.price_each
        if trade.type == Trade.sell:
            total_in_base_currency *= -1

        if trade.currency != self._config.currency.base_currency:
            date = trade.date
            iter_strategy = DATE_STRATEGY_FORWARD
            # Sometimes the stock market might close.
            # Always use future date first, if not, we traverse backwards
            # Does not handle no data case.
            while True:
                exchange_rate = self._db.query_price_stock_by_date_and_symbol(
                    date,
                    trade.currency,
                )
                if exchange_rate:
                    break

                if iter_strategy == DATE_STRATEGY_FORWARD:
                    arrow_date = arrow.get(date).shift(days=1)
                else:
                    arrow_date = arrow.get(date).shift(days=-1)

                if arrow_date > arrow.now():
                    iter_strategy = DATE_STRATEGY_BACKWARD
                date = arrow_date.format(self._config.download_config.date_format)

            total_in_base_currency *= exchange_rate

        return total_in_base_currency
