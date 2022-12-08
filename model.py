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

    def __str__(self):
        return "line: " + self.id + "\n" + "stations: " + str(self.stations)

    def random_station(self):
        return random.choice(self.stations)


class Lines:
    A = Line(
        "A",
        ["L'Etoile", 'Edmée Chandon', 'Denis Papin', 'Auguste Delaune', 'Marie Curie', 'La Rampe - Centre-Ville',
         'Echirolles Gare', 'Essarts - La Butte', 'Surieux', 'Les Granges', 'Polesud - Alpexpo', "Grand'place",
         'Arlequin', 'La Bruyère-Parc Jean Verlhac', 'Malherbe', 'MC2: Maison de la Culture', 'Mounier',
         'Albert 1er de Belgique', 'Chavant', 'Verdun - Préfecture', 'Hubert Dubedout - Maison du Tourisme',
         'Victor Hugo', 'Alsace-Lorraine', 'Gares', 'Saint-Bruno', 'Berriat-Le Magasin', 'Les Fontainades - Le Vog',
         'Louis Maisonnat', 'Fontaine Hôtel de Ville - La Source', 'Charles Michels', 'La Poya']

    )
    B = Line(
        "B",
        ['Plaine des Sports', 'Gières Gare - Universités', 'Mayencin - Champ Roman', 'Condillac - Universités',
         'Bibliothèques Universitaires', 'Gabriel Fauré', 'Les Taillées - Universités', 'Grand Sablon', 'Michallon',
         'La Tronche Hôpital', 'Ile Verte', 'Notre-Dame - Musée', 'Sainte-Claire - Les Halles',
         'Hubert Dubedout - Maison du Tourisme', 'Victor Hugo', 'Alsace-Lorraine', 'Gares', 'Saint-Bruno',
         'Palais de Justice - Gare', 'Cité Internationale', 'Marie-Louise Paris - CEA', 'Oxford']
    )
    C = Line(
        "C",
        ['Condillac - Universités', 'Bibliothèques Universitaires', 'Gabriel Fauré', 'Hector Berlioz - Universités',
         'Neyrpic - Belledonne', 'Péri - Brossolette', 'Flandrin - Valmy', 'Grenoble Hôtel de Ville', 'Chavant',
         'Gustave Rivet', 'Foch - Ferrié', 'Vallier - Libération', 'Vallier - Docteur Calmette', 'Vallier - Catane',
         'Seyssinet-Pariset Hôtel de Ville', 'Fauconnière', 'Grand Pré', 'Mas des Iles', 'Le Prisme']
    )
    D = Line(
        "D",
        ['Les Taillées - Universités', 'Neyrpic - Belledonne', 'Maison Communale', 'Edouard Vaillant',
         'Parc Jo Blanchon', 'Etienne Grappe']
    )
    E = Line(
        "E",
        ['Louise Michel', 'Alliés', 'Vallier - Libération', 'Condorcet', 'Alsace-Lorraine',
         'Annie Fratellini-Esplanade', 'Casamaures - Village', 'Hôtel de Ville', 'Horloge', 'Néron',
         'Fiancey - Prédieu', 'Muret', 'Pont de Vence', 'La Pinéa - St Robert', 'Karben', 'Rafour', 'Palluel']
    )
    lines = [A, B, C, D, E]

    def __init__(self):
        pass

    @staticmethod
    def random_line():
        choices = [.3, .25, .25, .1, .1]
        return random.choices(Lines.lines, weights=choices)[0]


def get_common_stations():
    """
    ignore
    :return: ignore
    """
    freq = dict()
    for i in Lines.lines:
        for j in i.stations:
            if j in freq:
                freq[j].append(i.id)
            else:
                freq[j] = [i.id]
    print(dict((k, v) for k, v in freq.items() if len(v) > 1))


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
