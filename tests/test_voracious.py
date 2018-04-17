import os
import tempfile
import context
import voracious.app


def test_tests_are_working():
    assert 1 == 1

def test_home_says_hello():
    assert home() == "hello"
