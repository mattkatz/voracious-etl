'''This is the app that will provice a web api on top of all the different
   members
'''
from voracious.entitymanager import EntityManager
import os
import sys
from pathlib import Path
from flask import Flask, jsonify, render_template
sys.path.append(Path(__file__).parent)
sys.path.append('..')
sys.path.append('../models')

app = Flask(__name__)
print(os.getcwd())
mp = Path(__file__) / '..'/ '..' / 'models'
em = EntityManager(models_path=mp.resolve())



@app.route('/')
def home():
    return "hello"


@app.route('/models/')
def models():
    return render_template('models.html', models=em.models)

# TODO get all the models listed in models
@app.route('/api/models/')
def model_index():
    '''Return all the models supported'''
    model_list = [model.__name__ for model in em.models]
    return jsonify({'entities': model_list})

    # TODO for each model, get all the properties and attributes of the module. 
    # TODO maybe we should get all the ones decorated with some decorator?
    # TODO or should we just ignore only ones decorated with a decorator?
    # 

if __name__ == '__main__':
    app.run(debug=true)
