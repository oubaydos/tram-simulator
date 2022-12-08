from datetime import datetime
from time import sleep

from kafka import KafkaProducer

from model import Validation, Client, Card, Lines

producer = KafkaProducer(bootstrap_servers='localhost:9092')
s = "hello"
while True:
    line = Lines.random_line()
    validation = Validation(Client.random(), Card.random(), line.random_station(), line.id, line.random_station(),
                            datetime.now().isoformat())
    producer.send('temp-topic', bytes(validation.to_json(), encoding='utf-8'))
    sleep(.1)
