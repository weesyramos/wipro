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