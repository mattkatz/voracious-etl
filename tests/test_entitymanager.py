import context
from voracious.entitymanager import EntityManager
import importlib
from pathlib import Path
from dataclasses import dataclass


class TestEntityManager:
    def test_get_module_from_path(self):
        # test a path that doesn't have a module
        assert EntityManager.get_module_from_path(Path('foo')) is None

        # test this file is a module
        assert EntityManager.get_module_from_path(Path(__name__)) 

        # test we get a module from a directory
        assert EntityManager.get_module_from_path(Path('models'))


    def test_get_data_classes_from_module(self):
        # there should be no classes in context
        classes = EntityManager.get_classes_from_module(
                importlib.import_module('context'))
        assert len(classes) == 0

        # There should be two dataclasses in this file
        classes = EntityManager.get_classes_from_module(
                importlib.import_module('test_entitymanager'))
        assert len(classes) == 2

    def test_is_dataclass(self):
        # this is not a dataclass
        assert not EntityManager.is_dataclass(EntityManager)
        # this is
        assert EntityManager.is_dataclass(Dumber)


@dataclass
class Dumb:
    foo: str


@dataclass
class Dumber:
    bar: str
