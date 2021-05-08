import argparse
import yaml

from google.protobuf import json_format
from generated.proto.config_pb2 import Config

def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="Balance your portfolio.")
    parser.add_argument(
        '--config',
        dest='config',
        default=os.environ.get('CONFIG'),
        type=str,
        required=True,
        help='Path to the config YAML file specification',
    )
    args = parser.parse_args()
    with open(args.config, "r") as file:
        return json_format.ParseDict(yaml.safe_load(file), Config())
