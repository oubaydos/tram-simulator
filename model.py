import json
from enum import Enum


class Subscription(str, Enum):
    Month = "Month"
    Day = "Day"
    Hour = "Hour"


class Client:
    id: str = None
    firstName: str = None
    lastName: str = None

    def __init__(self, id: str, firstName: str, lastName: str) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName


class Card:
    id: str = None
    type: Subscription = None
    endOfValidityTimeStamp: str = None

    def __init__(self, id: str, type: Subscription, endOfValidityTimeStamp: str):
        self.id = id
        self.type = type
        self.endOfValidityTimeStamp = endOfValidityTimeStamp


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
