from datetime import datetime
from time import sleep

from confluent_kafka import Producer

from config import kafka_endpoint, kafka_topic
from model import Validation, Client, Card, Lines

producer = Producer({'bootstrap.servers': kafka_endpoint})
while True:
    line = Lines.random_line()
    validation = Validation(Client.random(), Card.random(), line.random_station(), line.id, line.random_station(),
                            datetime.now().isoformat())
    producer.produce(kafka_topic, bytes(validation.to_json(), encoding='utf-8'))
    sleep(.1)
