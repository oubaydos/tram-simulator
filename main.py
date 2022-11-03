from datetime import datetime

from model import Validation, Client, Card


def main():
    # client = Client("4546er", "obaydah", "bouifadene")
    # card = Card("fes6", Subscription.get_random(), datetime.now().isoformat())
    validation = Validation(Client.random(), Card.random(), "chavant", "C", "condillac", datetime.now().isoformat())
    print(validation.toJSON())
    # generate_random_clients(1000)


if __name__ == '__main__':
    main()
