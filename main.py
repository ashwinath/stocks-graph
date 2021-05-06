import service.alphavantage
import db

from types import SimpleNamespace
from generated.proto.config_pb2 import Config

from config.parser import parse_args

def create_dependencies(config: Config) -> SimpleNamespace:
    quest_db = db.QuestDB(config.quest_db)
    return SimpleNamespace(
        quest_db=quest_db,
    )

def main():
    config = parse_args()
    dependencies = create_dependencies(config)
    for batch in service.alphavantage.download_data(config):
        dependencies.quest_db.write(batch)

if __name__ == "__main__":
    main()
