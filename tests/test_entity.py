import context
from models.entity import Entity


class TestEntity:
    def test_repr_is_code(self):
        entity = Entity(code='TESTENTITY')
        assert entity.__repr__() == 'Entity: TESTENTITY'
