import json
import random
import uuid
from enum import Enum

from data import clients


# should not be enum or str
class Lines(str, Enum):
    A = []  # list of stations of line A
    # ..


class Subscription(str, Enum):
    Month = "Month"
    Day = "Day"
    Hour = "Hour"

    @staticmethod
    def random():
        return random.choice(list(Subscription))


class Client:
    id: str = None
    firstName: str = None
    lastName: str = None

    def __init__(self, id: str, firstName: str, lastName: str) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

    @staticmethod
    def random():
        random_client = random.choice(clients)
        return Client(random_client[0], random_client[1], random_client[2])


class Card:
    id: str = None
    type: Subscription = None
    endOfValidityTimeStamp: str = None

    def __init__(self, id: str, type: Subscription, endOfValidityTimeStamp: str):
        self.id = id
        self.type = type
        self.endOfValidityTimeStamp = endOfValidityTimeStamp

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

    def __init__(self, client: Client, card: Card, stationId: str, line: str, destinationStationId: str,
                 requestTimeStamp: str):
        self.client = client
        self.card = card
        self.stationId = stationId
        self.line = line
        self.destinationStationId = destinationStationId
        self.requestTimeStamp = requestTimeStamp

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
