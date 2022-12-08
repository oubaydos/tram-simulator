import json
from time import sleep

from kafka import KafkaConsumer

from config import kafka_endpoint, kafka_topic
from model import Validation

consumer = KafkaConsumer(bootstrap_servers=kafka_endpoint)
consumer.subscribe(topics=[kafka_topic])
for msg in consumer:
    v: Validation = json.loads(msg.value)
    print(v["client"])
