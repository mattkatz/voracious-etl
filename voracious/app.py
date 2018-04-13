from flask import Flask
from .entitymanager import EntityManager


app = Flask(__name__)


class WebApi:
    '''This is the app that will provice a web api on top of all the different
       members
    '''
    def __init__(self, models_path: str):
        self.models_path = models_path
        self.em = EntityManager(models_path)

    @app.route('/')
    def home(self):
        return "hello"

    # TODO get all the models listed in models
    @app.route('/index')
    def model_index(self):
        '''Return all the models supported'''
        return self.em.models

    # TODO for each model, get all the properties and attributes of the module. 
    # TODO maybe we should get all the ones decorated with some decorator?
    # TODO or should we just ignore only ones decorated with a decorator?
    # 
