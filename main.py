import db
import service.alphavantage
import service.yahoo
import logger

from config.parser import parse_args
from generated.proto.config_pb2 import Config
from types import SimpleNamespace

def create_dependencies(config: Config) -> SimpleNamespace:
    timescale_db = db.TimescaleDB(config.timescale_db)
    return SimpleNamespace(
        timescale_db=timescale_db,
    )

def download_stocks_data(config, dependencies):
    download_functions = [
        service.alphavantage.download_data,
        service.yahoo.download_data,
    ]
    for download_function in download_functions:
        for batch in download_function(config):
            dependencies.timescale_db.write(batch)

def main():
    logger.init_logger()
    config = parse_args()
    dependencies = create_dependencies(config)
    download_stocks_data(config, dependencies)

if __name__ == "__main__":
    main()
