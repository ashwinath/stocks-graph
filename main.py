import service.alphavantage

from config.parser import parse_args

if __name__ == "__main__":
    config = parse_args()
    data = service.alphavantage.download_data(config)

    import pprint
    pprint.pprint(data)
