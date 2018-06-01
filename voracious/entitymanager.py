'''TODO This class should provide a list of classes or models
   help store them, provide datatable names, etc
'''

from pathlib import Path
import inspect
import importlib
import os
import sys


class EntityManager(object):
    '''Manages the list of entities for us - should also know which are remote
       or local
    '''

    def __init__(self, models_path='models'):
        '''Starts up and iterates over all files in dir and gets a list of
           classes available
        '''
        self.models_path = Path(models_path)
        print(f'getting models from {models_path}')
        # find files in models directory
        self.models = [self.get_struct_from_type(model) for model in 
                self.get_models_from_path(self.models_path)]

    @classmethod
    def get_struct_from_type(cls, entity_type):
        ''' returns a data representation of a type
        '''
        # expects a dataclass field so...
        name = entity_type.__name__
        fields = [fieldname for fieldname, field in  entity_type.__dataclass_fields__.items()]
        return {'name':name, 'fields': fields}

    @classmethod
    def get_module_from_path(cls, path):
        '''returns a Module from a pathlib path or returns None if there's
           no module there
        '''
        print('enter get_module_from_path')
        print(f'path: {path}')
        if not path.exists(): 
            print(f'{path} does not exist')
            return None
        if cls.is_dunder(path.stem):
            # ignore __pycache__ and __init__.py and __main__ and the like
            return None

        # lets get the path from here to there
        strpath = os.path.relpath(path)
        relpath = Path(strpath)
        print(f'relpath = {relpath}')
        # transform to path notation
        module_parts = list(relpath.parts)
        module_parts[-1] = relpath.stem
        module_path = '.'.join(module_parts)
        print(f'trying {module_path}')
        module = None
        try:
            module = importlib.import_module(module_path )
            # module = importlib.import_module(path.stem)
        except ModuleNotFoundError as e:
            print(os.getcwd())
            print(sys.path)
            print(e)
            print('exit none from get_module_from_path')
        finally:
            print('exit get_module_from_path')
            return module

    @classmethod
    def get_models_from_path(cls, models_path):
        '''returns model classes found recusively in a Path'''
        print('enter get_models_from_path')
        print(f'models_path: {models_path}')

        models = []
        if cls.is_dunder(models_path.stem): return models
        if models_path.is_dir():
            models.extend(cls.get_models_from_dir(models_path))
        models.extend(cls.get_models_from_file(models_path))
        print('exit get_models_from_path')
        return models

    @classmethod
    def get_models_from_file(cls, file_path):
        '''Returns an array of all dataclass models in a file '''
        print('enter get_models_from_file')
        print(f'file_path: {file_path}')
        models = []
        if not cls.is_dunder(file_path.name) and file_path.suffix == '.py':
            module = cls.get_module_from_path(file_path)
            print(module)
            if module:
                models.extend(cls.get_classes_from_module(module))
        print('exit get_models_from_file')
        return models

    @classmethod
    def get_models_from_dir(cls, dir_path):
        '''recursively gets all dataclass models from a directory'''
        print('enter get_models_from_dir')
        print(f'dir_path: {dir_path}')
        models = []
        for item in dir_path.iterdir():
            print(item)
            models.extend(cls.get_models_from_path(item))
        print('exit get_models_from_dir')
        return models

    @classmethod
    def get_classes_from_module(cls, module):
        '''Returns all the dataclasses in a module.
           Examines each class in a module to see if it is a dataclasss

           Accepts a Module from importlib
        '''
        print('enter get_classes_from_module')
        print(f'module: {module}')
        classes = []
        for name in dir(module):
            obj = getattr(module, name)
            if cls.is_dataclass(obj):
                classes.append(obj)
        print('exit get_classes_from_module')
        return classes

    @classmethod
    def is_dataclass(cls, obj):
        '''Returns if this object is a dataclass.
           Assumes all Dataclasses will have an __annotations__ attribute
        '''
        return inspect.isclass(obj) and obj.__dict__.get('__annotations__')

    @classmethod
    def is_dunder(cls, name):
        return name.startswith('__') and name.endswith('__')
