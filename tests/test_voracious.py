import os
import tempfile
import context
import voracious.app


def client():
    return voracious.app.test_client()

def test_tests_are_working():
    assert 1 == 1

def test_home_says_hello(client):
    rv = client.get('/')
    assert rv.data  == "hello"
