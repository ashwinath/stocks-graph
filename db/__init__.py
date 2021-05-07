import psycopg2
import psycopg2.pool
from datetime import datetime

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
                    price  DOUBLE PRECISION NOT NULL
                );
                """
            )
            connection.commit()
        finally:
            if connection:
                connection.close()
            if cursor:
                cursor.close()

    def write(self, stock_data_bulk):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            # TODO: change to bulk insert
            for stock in stock_data_bulk:
                cursor.execute("""
                    INSERT INTO stocks_history
                    VALUES (%s, %s, %s, %s);
                    """,
                    (
                        stock["ts"],
                        stock["date"],
                        stock["symbol"],
                        stock["price"],
                    ),
                )
            connection.commit()
            cursor.execute("SELECT * FROM stocks_history;")
            records = cursor.fetchall()
            for row in records:
                print(row)
        finally:
            if connection:
                connection.close()
            if cursor:
                cursor.close()
