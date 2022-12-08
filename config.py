import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\oubay\\OneDrive\\Bureau\\projects\\tram-simulator\\env.ini')
kafka_url = config.get("ValidationService", "kafka-url")
kafka_port = config.get("ValidationService", "kafka-port")
kafka_endpoint = kafka_url + ":" + kafka_port
kafka_topic = config.get("ValidationService", "kafka-topic")
