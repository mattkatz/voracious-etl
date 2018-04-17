'''This is the app that will provice a web api on top of all the different
   members
'''
import os
import sys
from pathlib import Path
from flask import Flask
sys.path.append(Path(__file__).parent)
from voracious.entitymanager import EntityManager
sys.path.append('..')
sys.path.append('../models')

app = Flask(__name__)
print(os.getcwd())
mp = Path(__file__) / '..'/ '..' / 'models'
em  = EntityManager(models_path=mp.resolve())



@app.route('/')
def home():
    return "hello"

# TODO get all the models listed in models
@app.route('/index')
def model_index():
    '''Return all the models supported'''
    resp = f'We have {len(em.models)} models'
    model_list = ''.join([f'<li>{model.__name__}</li>' for model in em.models])
    print(model_list)
    resp += f'<ul>{model_list}</ul>'
    return resp

    # TODO for each model, get all the properties and attributes of the module. 
    # TODO maybe we should get all the ones decorated with some decorator?
    # TODO or should we just ignore only ones decorated with a decorator?
    # 
