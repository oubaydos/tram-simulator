import json
from time import sleep

from kafka import KafkaConsumer

from config import kafka_endpoint, kafka_topic
from model import Validation

consumer = KafkaConsumer(bootstrap_servers=kafka_endpoint)
consumer.subscribe(topics=[kafka_topic])
counter = 0
for msg in consumer:
    counter += 1
    if counter == 8:
        break
    v: Validation = json.loads(msg.value)
    #print(v["client"])
    print(v)
