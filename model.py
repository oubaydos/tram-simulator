import json


class Client:
    id = None
    firstName = None
    lastName = None

    def __init__(self, id: str, firstName: str, lastName: str) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName


class Card:
    id = None
    type = None
    endOfValidityTimeStamp = None

    def __init__(self, id: str, type: str, endOfValidityTimeStamp: str):
        self.id = id
        self.type = type
        self.endOfValidityTimeStamp = endOfValidityTimeStamp


class Validation:
    client = None
    card = None
    stationId = None
    line = None
    destinationStationId = None
    requestTimeStamp = None

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
