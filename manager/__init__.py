from abc import abstractmethod
from db import TimescaleDB
from generated.proto.config_pb2 import Config

class Manager(object):
    def __init__(self, config: Config, db: TimescaleDB):
        self._config = config
        self._db = db

    @abstractmethod
    def process(self, *args, **kwargs):
        pass
