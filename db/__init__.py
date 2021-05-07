import psycopg2
import psycopg2.pool

from typing import List

class TimescaleDB(object):
    def __init__(self, config):
        self._db =  psycopg2.pool.ThreadedConnectionPool(
            minconn=config.min_connections,
            maxconn=config.max_connections,
            user=config.user,
            password=config.password,
            host=config.host,
            port=config.port,
            database=config.database,
        )
        self.init_tables()

    def init_tables(self):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stocks_history (
                    time   TIMESTAMP NOT NULL,
                    date   DATE NOT NULL,
                    symbol TEXT NOT NULL,
                    price  DOUBLE PRECISION NOT NULL,
                    currency TEXT NOT NULL,
                    CONSTRAINT unique_date_symbol UNIQUE (date, symbol)
                );
                """
            )
            cursor.execute("DROP TABLE IF EXISTS trades;")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS trades (
                    time   TIMESTAMP NOT NULL,
                    date   DATE NOT NULL,
                    symbol TEXT NOT NULL,
                    price_each  DOUBLE PRECISION NOT NULL,
                    quantity INTEGER NOT NULL,
                    currency TEXT NOT NULL,
                    total_in_base_currency DOUBLE PRECISION NOT NULL
                );
                """
            )
            connection.commit()
        finally:
            if connection:
                self._db.putconn(connection)
            if cursor:
                cursor.close()

    def save_stocks(self, stock_data_bulk):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            for stock in stock_data_bulk:
                cursor.execute("""
                    INSERT INTO stocks_history
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING;
                    """,
                    (
                        stock["ts"],
                        stock["date"],
                        stock["symbol"],
                        stock["price"],
                        stock["currency"],
                    ),
                )
            connection.commit()
        finally:
            if connection:
                self._db.putconn(connection)
            if cursor:
                cursor.close()

    def query_price_stock_by_date_and_symbol(self, date: str, symbol: str):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT
                    price
                FROM
                    stocks_history
                WHERE
                    symbol = %(symbol)s
                    AND date = %(date)s
                LIMIT 1;
                """,
                {
                    "symbol": symbol,
                    "date": date,
                }
            )
            result = cursor.fetchone()
            return result[0] if result is not None else None
        finally:
            if connection:
                self._db.putconn(connection)
            if cursor:
                cursor.close()

    def save_trades(self, trade_data_bulk: List[dict]):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            for stock in trade_data_bulk:
                cursor.execute("""
                    INSERT INTO trades
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """,
                    (
                        stock["ts"],
                        stock["date"],
                        stock["symbol"],
                        stock["price_each"],
                        stock["quantity"],
                        stock["currency"],
                        stock["total_in_base_currency"],
                    ),
                )
            connection.commit()
        finally:
            if connection:
                self._db.putconn(connection)
            if cursor:
                cursor.close()
