import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

kafka_url = os.environ.get("KAFKA_URL")
kafka_port = os.environ.get("KAFKA_PORT")
kafka_endpoint = kafka_url + ":" + kafka_port
kafka_topic = os.environ.get("KAFKA_TOPIC")
