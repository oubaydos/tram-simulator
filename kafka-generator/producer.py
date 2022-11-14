from datetime import datetime
from time import sleep

from kafka import KafkaProducer

from model import Validation, Client, Card

producer = KafkaProducer(bootstrap_servers='localhost:9092')
s = "hello"
for i in range(100):
    validation = Validation(Client.random(), Card.random(), "chavant", "C", "condillac", datetime.now().isoformat())
    producer.send('temp-topic', bytes(validation.to_json(),encoding='utf-8'))
    sleep(2)
