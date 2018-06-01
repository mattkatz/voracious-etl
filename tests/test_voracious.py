import context
import pytest
from voracious.app import app, EntityManager
from unittest.mock import patch
from tests.dummy_models.dummies import Dumb, Dumber


@pytest.fixture
def client():
    client = app.test_client()
    client.testing = True
    return client


def test_tests_are_working():
    assert 1 == 1


def test_home_says_hello(client):
    rv = client.get('/')
    assert rv.data == b"hello"


def test_web_index(client):
    with patch('voracious.app.em') as mock_em:
        mock_em.models = {'Dumb': Dumb, 'Dumber': Dumber}
        rv = client.get('/models/')
        assert b'Dumb' in rv.data
        assert b'Dumber' in rv.data


def test_api_index(client):
    with patch('voracious.app.em') as mock_em:
        mock_em.models = [EntityManager.get_struct_from_type(Dumb),
                          EntityManager.get_struct_from_type(Dumber)]
        rv = client.get('/api/entities/')
        assert b'Dumb' in rv.data
        assert b'Dumber' in rv.data
