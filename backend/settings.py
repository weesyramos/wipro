# coding: utf-8
from prettyconf import config


ENVIRONMENT='Development'
DEBUG=True
TESTING=True
PORT = config("PORT", default=5000)