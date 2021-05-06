import psycopg2
import psycopg2.pool
from datetime import datetime

class QuestDB(object):
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
        pass

    def write(self):
        connection = None
        cursor = None
        try:
            connection = self._db.getconn()
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS trades (ts TIMESTAMP, date DATE, name STRING, value INT) timestamp(ts);")
            # insert 10 records
            for x in range(10):
              now = datetime.utcnow()
              date = datetime.now().date()
              cursor.execute("""
                INSERT INTO trades
                VALUES (%s, %s, %s, %s);
                """, (now, date, "python example", x))
            # commit records
            connection.commit()
            cursor.execute("SELECT * FROM trades;")
            records = cursor.fetchall()
            for row in records:
                print(row)
        finally:
            if connection:
                connection.close()
            if cursor:
                cursor.close()
