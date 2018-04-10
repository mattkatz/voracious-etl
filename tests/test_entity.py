import context
from models.entity import Entity


class TestEntity:

    def test_get_entity_fields(self):
        assert Entity.field_names() == ['id', 'code']
