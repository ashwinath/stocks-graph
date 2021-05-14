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
            cursor.execute("DROP INDEX IF EXISTS stats_time_ix;")
            cursor.execute("DROP TABLE IF EXISTS stats;")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stats (
                    time   TIMESTAMP NOT NULL,
                    date   DATE NOT NULL,
                    symbol TEXT NOT NULL,
                    principal  DOUBLE PRECISION,
                    nav DOUBLE PRECISION,
                    returns_percentage DOUBLE PRECISION
                );
                """
            )
            cursor.execute("CREATE INDEX stats_time_ix ON stats(time);")
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

    def save_stats(self, stats_data_bulk: List[dict]):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            for stats in stats_data_bulk:
                cursor.execute("""
                    WITH a AS (
                        SELECT
                            SUM(quantity) AS qty,
                            SUM(total_in_base_currency) AS principal
                        FROM
                            trades
                        WHERE
                            date <= %(date)s
                            AND symbol = %(symbol)s
                        LIMIT 1
                    ),
                    forex AS (
                        SELECT COALESCE(
                            (
                                SELECT
                                    price
                                FROM
                                    stocks_history
                                WHERE
                                    date <= %(date)s
                                    AND symbol = (
                                        SELECT
                                            currency
                                        FROM
                                            stocks_history
                                        WHERE
                                            date = %(date)s
                                            AND symbol = %(symbol)s
                                        LIMIT 1
                                    )
                                LIMIT 1
                            ),
                            1
                        ) AS exchange_rate
                        LIMIT 1
                    )
                    INSERT INTO
                        stats (
                            time,
                            date,
                            symbol,
                            principal,
                            nav,
                            returns_percentage
                        )
                    SELECT
                        time,
                        date,
                        symbol,
                        a.principal AS principal,
                        a.qty * stocks_history.price * forex.exchange_rate AS nav,
                        CASE
                            WHEN a.qty = 0 THEN 0
                            ELSE ((a.qty * stocks_history.price * forex.exchange_rate) - a.principal) / a.principal * 100
                        END AS returns_percentage
                    FROM
                        a, stocks_history, forex
                    WHERE
                        stocks_history.date = %(date)s
                        AND symbol = %(symbol)s
                    LIMIT 1;
                    """,
                    stats,
                )
            connection.commit()
        finally:
            if connection:
                self._db.putconn(connection)
            if cursor:
                cursor.close()

    def query_date_symbol_paginated(self, limit: int, offset: int):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            cursor.execute(f"""
                SELECT
                    date,
                    symbol
                FROM
                    stocks_history
                WHERE
                    symbol in (
                        SELECT
                            DISTINCT(symbol)
                        FROM
                            trades
                    )
                ORDER BY
                    date,
                    symbol
                limit {limit}
                offset {offset};
                """,
            )
            results = cursor.fetchall()
            return [
                {
                    "date": result[0],
                    "symbol": result[1],
                } for result in results
            ]

        finally:
            if connection:
                self._db.putconn(connection)
            if cursor:
                cursor.close()
