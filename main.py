import service.alphavantage
import db

from types import SimpleNamespace

from config.parser import parse_args

def create_dependencies(config):
    quest_db = db.QuestDB(config.quest_db)
    return SimpleNamespace(
        quest_db=quest_db,
    )

def main():
    config = parse_args()
    dependencies = create_dependencies(config)
    dependencies.quest_db.write()
    data = service.alphavantage.download_data(config)

    import pprint
    pprint.pprint(data)

if __name__ == "__main__":
    main()
