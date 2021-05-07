import db
import service.alphavantage

from config.parser import parse_args
from generated.proto.config_pb2 import Config
from types import SimpleNamespace

def create_dependencies(config: Config) -> SimpleNamespace:
    timescale_db = db.TimescaleDB(config.timescale_db)
    return SimpleNamespace(
        timescale_db=timescale_db,
    )

def main():
    config = parse_args()
    dependencies = create_dependencies(config)
    for batch in service.alphavantage.download_data(config):
        dependencies.timescale_db.write(batch)

if __name__ == "__main__":
    main()
