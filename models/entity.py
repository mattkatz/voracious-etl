import inspect
from dataclasses import dataclass, field, fields
from uuid import UUID, uuid4

@dataclass
class Entity(object):
    ''' This is the base entity that all others can inherit from'''
    # id: UUID = field(default_factory=uuid4())
    id: int
    code: str 


    @classmethod
    def field_names(cls):
        return [field.name for field in fields(cls)]
