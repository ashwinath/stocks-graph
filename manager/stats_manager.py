import logging

from . import Manager

class StatsManager(Manager):
    def process(self):
        logging.info("Processing stats")
        offset = 0
        batch_size = self._config.stats.batch_size;

        while True:
            result = self._db.query_date_symbol_paginated(batch_size, offset)
            if not result:
                break
            self._db.save_stats(result)
            offset += batch_size

        logging.info("Done processing stats")
