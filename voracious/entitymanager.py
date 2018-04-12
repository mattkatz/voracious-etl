'''TODO This class should provide a list of classes or models
   help store them, provide datatable names, etc
'''

from pathlib import Path
import inspect
import importlib


class EntityManager(object):
    '''Manages the list of entities for us - should also know which are remote
       or local
    '''

    def __init__(self, models_path='models'):
        '''Starts up and iterates over all files in dir and gets a list of
           classes available
        '''
        self.models_path = Path(models_path)
        self.models = []
        # TODO find files in models directory

        # TODO for each file in models dir get classes in file

    @classmethod
    def get_module_from_path(cls, path):
        '''returns a model from a pathlib path or returns None'''
        module = path.stem
        try:
            return importlib.import_module(module)
        except:
            return None

    @classmethod
    def get_models_from_dir(cls, models_path, models):
        '''Adds model classes found in a path to an array passed in
           returns the array
        '''
        models = []
        for item in models_path.iterdir():
            module = cls.get_module_from_path(item)
            if not module and item.is_dir():
                # recurse
                cls.get_models_from_dir(item, models)
            models.append(cls.get_classes_from_file)

    @classmethod
    def get_classes_from_module(cls, module):
        classes = []
        for name in dir(module):
            obj = getattr(module, name)
            if cls.is_dataclass(obj):
                classes.append(obj)
        return classes

    @classmethod
    def is_dataclass(cls, obj):
        return inspect.isclass(obj) and obj.__dict__.get('__annotations__')
