import context
from voracious.app import WebApi


class TestVoracious:
    def test_tests_are_working(self):
        assert 1 == 1

    def test_home_says_hello(self):
        wb = WebApi()
        # from context import voracious.app.WebApi as wb
        assert wb.home() == "hello"
