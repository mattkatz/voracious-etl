import inspect


class Entity(object):
    ''' This is the base entity that all others can inherit from'''
    id = 0
    code = ''

    @classmethod
    def fields(cls):
        return [name for name, item in inspect.getmembers(cls,
                lambda x: not inspect.isfunction(x)) if not
                (name.endswith('__') and name.startswith('__'))]

    def __repr__(self):
        return f'Entity: {self.code}'

