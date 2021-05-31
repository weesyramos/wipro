# coding: utf-8
from prettyconf import config


MAIN_URL_CODE_CHALLENGER='http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json'
ENVIRONMENT='Development'
DEBUG=True
TESTING=True
PORT = config("PORT", default=5000)