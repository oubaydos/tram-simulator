from datetime import datetime

from model import Validation, Client, Card


def main():
    client = Client("4546er", "obaydah", "bouifadene")
    card = Card("fes6", "subscription", datetime.now().isoformat())
    validation = Validation(client, card, "chavant", "C", "condillac", datetime.now().isoformat())
    print(validation.toJSON())


if __name__ == '__main__':
    main()
