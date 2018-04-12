from flask import Flask


app = Flask(__name__)


class WebApi:
    '''This is the app that will provice a web api on top of all the different
       members
    '''

    @app.route('/')
    def home(self):
        return "hello"

    # TODO get all the models listed in models
    def model_index(self):
        '''Return all the models supported'''

    # TODO for each model, get all the properties and attributes of the module. 
    # TODO maybe we should get all the ones decorated with some decorator?
    # TODO or should we just ignore only ones decorated with a decorator?
    # 
