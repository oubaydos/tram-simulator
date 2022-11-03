import json
import random
import uuid
from enum import Enum

from data import clients


# should not be enum or str
# line = character(A,B..) + list of stations included
class Line:
    id: str = None
    stations: list = []

    def __init__(self, _id: str, stations: list):
        assert len(_id) < 4
        self.id = _id
        self.stations = stations


class Subscription(str, Enum):
    Month = "Month"
    Day = "Day"
    OneTimeUse = "OneTimeUse"
    Year = "Year"

    @staticmethod
    def random():
        return random.choice(list(Subscription))


class Client:
    id: str = None
    firstName: str = None
    lastName: str = None

    def __init__(self, _id: str, firstname: str, lastname: str) -> None:
        self.id = _id
        self.firstName = firstname
        self.lastName = lastname

    @staticmethod
    def random():
        random_client = random.choice(clients)
        return Client(random_client[0], random_client[1], random_client[2])


class Card:
    id: str = None
    type: Subscription = None
    endOfValidityTimeStamp: str = None

    def __init__(self, _id: str, subscription_type: Subscription, end_of_validity_timestamp: str):
        self.id = _id
        self.type = subscription_type
        self.endOfValidityTimeStamp = end_of_validity_timestamp

    @staticmethod
    def random():
        from random_generator import random_end_of_life_timestamp
        temp_type = Subscription.random()
        return Card(uuid.uuid4().hex, temp_type, random_end_of_life_timestamp(temp_type))


class Validation:
    client: Client = None
    card: Card = None
    stationId: str = None
    line: str = None
    destinationStationId: str = None
    requestTimeStamp: str = None

    def __init__(self, client: Client, card: Card, station_id: str, line: str, destination_station_id: str,
                 request_timestamp: str):
        self.client = client
        self.card = card
        self.stationId = station_id
        self.line = line
        self.destinationStationId = destination_station_id
        self.requestTimeStamp = request_timestamp

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
