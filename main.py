import db
import logger
import service.yahoo
import service.alphavantage

from config.parser import parse_args
from config.trades import get_all_trade_configs
from generated.proto.config_pb2 import Config
from manager.trade_manager import TradeManager
from types import SimpleNamespace

def create_dependencies(config: Config) -> SimpleNamespace:
    timescale_db = db.TimescaleDB(config.timescale_db)
    trade_manager = TradeManager(config, timescale_db)
    return SimpleNamespace(
        timescale_db=timescale_db,
        trade_manager=trade_manager,
    )

def download_data(config, dependencies):
    download_functions = [
        service.alphavantage.download_data,
        service.yahoo.download_data,
        service.alphavantage.download_foreign_exchange,
    ]
    for download_function in download_functions:
        for batch in download_function(config):
            dependencies.timescale_db.save_stocks(batch)

def main():
    logger.init_logger()
    config = parse_args()

    dependencies = create_dependencies(config)
    download_data(config, dependencies)

    trades = get_all_trade_configs(config)
    dependencies.trade_manager.process(trades)

if __name__ == "__main__":
    main()
