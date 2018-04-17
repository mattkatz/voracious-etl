import importlib
from pathlib import Path
import context
from voracious.entitymanager import EntityManager as em
# from context import EntityManager as em


class Testem:
    def test_get_module_from_path(self):
        # test a path that doesn't have a module
        assert em.get_module_from_path(Path('foo')) is None

        # test this file is a module
        mod = em.get_module_from_path(Path(__file__)) 
        print(mod)
        assert mod
        assert len([name for name in dir(mod) if not em.is_dunder(name)]) > 0

        # test we get a module from a directory
        assert em.get_module_from_path(Path('models'))

    def test_get_models_from_path(self):
        # test with no models
        path = Path(__file__)
        models = em.get_models_from_path(path)
        assert len(models) == 0
        # test a directory
        path = path.parent / 'dummy_models'
        models = em.get_models_from_path(path)
        assert len(models) == 2
        # test a file
        path = path / 'dummies.py'
        models = em.get_models_from_path(path)
        assert len(models) == 2

    def test_get_models_from_file(self):
        path = Path(__file__).parent / 'dummy_models' / 'dummies.py'
        models = em.get_models_from_file(path)
        assert len(models) == 2

    def test_get_models_from_dir(self):
        dummy_models_path = Path(__file__).parent / 'dummy_models'
        models = em.get_models_from_dir(dummy_models_path)
        assert len(models) == 2

    def test_get_data_classes_from_module(self):
        # there should be no classes in context
        classes = em.get_classes_from_module(
                importlib.import_module('context'))
        assert len(classes) == 0

        # There should be two dataclasses in this file
        classes = em.get_classes_from_module(
                importlib.import_module('dummy_models.dummies'))
        assert len(classes) == 2

    def test_is_dataclass(self):
        # this is not a dataclass
        assert not em.is_dataclass(em)
        # this is
        from dummy_models.dummies import Dumber
        assert em.is_dataclass(Dumber)

    def test_is_dunder(self):
        assert em.is_dunder('__foo__')
        assert not em.is_dunder('_foo_')
        assert not em.is_dunder('__foo')
        assert not em.is_dunder('foo__')
        assert not em.is_dunder('foo')

    def test_entity_manager_works(self):
        manager = em(models_path=Path('tests/dummy_models'))
        assert len(manager.models) == 2
        manager = em(models_path='tests/dummy_models')
        assert len(manager.models) == 2
