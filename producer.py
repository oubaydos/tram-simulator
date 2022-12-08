from datetime import datetime

from confluent_kafka import Producer

from config import kafka_endpoint, kafka_topic
from model import Validation, Client, Card, Lines

producer = Producer({'bootstrap.servers': kafka_endpoint})
while True:
    line = Lines.random_line()
    validation = Validation(Client.random(), Card.random(), line.random_station(), line.id, line.random_station(),
                            datetime.now().isoformat())
    producer.poll(.1)
    producer.produce(kafka_topic, bytes(validation.to_json(), encoding='utf-8'))
    producer.flush()
