import os
import yaml

from google.protobuf import json_format
from generated.proto.trades_pb2 import TradeHistory
from generated.proto.config_pb2 import Config

from typing import List

def get_all_trade_configs(config: Config) -> List[TradeHistory]:
    all_trade_histories = []
    for dir_path, dir_names, file_names in os.walk(config.trades.folder):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, "r") as file:
                trade_history = json_format.ParseDict(
                    yaml.safe_load(file),
                    TradeHistory(),
                )
                all_trade_histories.append(trade_history)
    return all_trade_histories
