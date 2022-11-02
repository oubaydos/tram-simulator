import requests

from config import endpoint
from model import Validation


def send_json(validation: Validation):
    requests.post(url=endpoint, data=validation.toJSON())
