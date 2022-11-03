import datetime
from datetime import timedelta
from random import randrange

import names
from dateutil.relativedelta import relativedelta

from model import Subscription


def random_date(start, end):
    """
    should return a normal law distribution that peaks in now()
    but instead returns a uniform distribution
    :param start: start date
    :param end: end date
    :return: random date between start and end
    """
    if start == end:
        return start
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_end_of_life_timestamp(subscription_type):
    """
    :param subscription_type: Subscription type: Monthly, Daily, OneTime (hourly)
    :return: a valid/invalid random end of life timestamp that could be in the past/present/future
    """
    min = datetime.datetime.now() - relativedelta(years=6)
    if subscription_type == Subscription.Month:
        max = datetime.datetime.now() + relativedelta(months=1)
    elif subscription_type == Subscription.Day:
        max = datetime.datetime.now() + relativedelta(days=1)
    else:
        max = datetime.datetime.now() + relativedelta(hours=1)
    return random_date(min, max).isoformat()


def generate_random_clients(number_of_clients: int) -> set:
    s = set()
    for i in range(number_of_clients):
        s.add(names.get_full_name())
    print(s)
    return s
