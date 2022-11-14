import json
from time import sleep

from kafka import KafkaConsumer

from model import Validation

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(topics=["temp-topic"])
for msg in consumer:
    v: Validation = json.loads(msg.value)
    print(v["client"])
