import datetime
import random
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
    now = int(datetime.datetime.now().timestamp())
    l = [randrange(start=int(start.timestamp()), stop=now), randrange(start=now, stop=int(end.timestamp()))]
    proba = [0.02, 0.98]
    return datetime.datetime.fromtimestamp(random.choices(l, weights=proba)[0])


def random_end_of_life_timestamp(subscription_type):
    """
    :param subscription_type: Subscription type: Monthly, Daily, OneTime (hourly)
    :return: a valid/invalid random end of life timestamp that could be in the past/present/future
    """
    min_time = datetime.datetime.now() - relativedelta(years=6)
    if subscription_type == Subscription.Month:
        max_time = datetime.datetime.now() + relativedelta(months=1)
    elif subscription_type == Subscription.Day:
        max_time = datetime.datetime.now() + relativedelta(days=1)
    elif subscription_type == Subscription.Year:
        max_time = datetime.datetime.now() + relativedelta(years=1)
    else:
        max_time = datetime.datetime.now() + relativedelta(hours=1)
    return random_date(min_time, max_time).isoformat()


def generate_random_clients(number_of_clients: int) -> set:
    s = set()
    for i in range(number_of_clients):
        s.add(names.get_full_name())
    print(s)
    return s


