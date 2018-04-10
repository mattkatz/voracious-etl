import context
from models.entity import Entity


class TestEntity:

    def test_get_entity_fields(self):
        assert Entity.field_names() == ['id', 'code']

    def test_entity_id_is_UUID(self):
        ent = Entity(code='TESTENTITY')
        id = ent.id
        assert type(id).__name__ == 'UUID'
