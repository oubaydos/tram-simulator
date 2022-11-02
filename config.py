import configparser

config = configparser.ConfigParser()
config.read('env.ini')
endpoint = config.get("ValidationService", "endpoint")
