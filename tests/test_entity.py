import context
from models.entity import Entity
from models.substance import Substance


class TestEntity:

    def test_get_entity_fields(self):
        assert Entity.field_names() == ['id', 'code']

    def test_entity_id_is_UUID(self):
        ent = Entity(code='TESTENTITY')
        id = ent.id
        assert type(id).__name__ == 'UUID'


class TestSubstance:

    def test_get_substance_fields(self):
        # we need to check that we are getting class fields, not parent
        assert Substance.field_names() == ['id', 'code', 'name', 'rating']
