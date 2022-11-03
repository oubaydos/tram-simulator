from datetime import datetime

from model import Validation, Client, Card, Subscription
import names


def generate_random_clients(number_of_clients: int) -> set:
    s = set()
    for i in range(number_of_clients):
        s.add(names.get_full_name())
    print(s)
    return s


def main():
    client = Client("4546er", "obaydah", "bouifadene")
    card = Card("fes6", Subscription.Month, datetime.now().isoformat())
    validation = Validation(client, card, "chavant", "C", "condillac", datetime.now().isoformat())
    print(validation.toJSON())
    # generate_random_clients(1000)


if __name__ == '__main__':
    main()
