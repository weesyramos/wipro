import pytest

from backend import settings
from unittest import mock
from webtest import TestApp


@pytest.fixture(scope='session')
def client(app):
    return TestApp(app)


@pytest.fixture(scope='session')
def app(request):
    from backend import create_app
    app = create_app()

    return app

@pytest.fixture()
def main_url_zap_imoveis():
    return settings.MAIN_URL_ZAP

@pytest.fixture()
def main_url_viva_real():
    return settings.MAIN_URL_VIVA_REAL