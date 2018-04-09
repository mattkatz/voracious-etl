import inspect
from uuid import uuid4


class Entity(object):
    ''' This is the base entity that all others can inherit from'''
    id = 0
    code = ''

    def __init__(self, code):
        self.code = code
        self.id = uuid4()


    @classmethod
    def fields(cls):
        return [name for name, item in inspect.getmembers(cls,
                lambda x: not inspect.isfunction(x)) if not
                (name.endswith('__') and name.startswith('__'))]

    def __repr__(self):
        return f'Entity: {self.code}'

