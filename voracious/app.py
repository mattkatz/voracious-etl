'''This is the app that will provice a web api on top of all the different
   members
'''
from voracious.entitymanager import EntityManager
import os
import sys
from pathlib import Path
from flask import Flask, jsonify, render_template
sys.path.append(str(Path(__file__).parent))

app = Flask(__name__)
print(os.getcwd())
mp = Path(__file__).parent / 'models'
em = EntityManager(models_path=mp.resolve())


@app.route('/')
def home():
    return "hello"


@app.route('/models/')
def models():
    return render_template('models.html', models=em.models)


@app.route('/api/entities/')
def model_index():
    '''Return all the entities supported'''
    # return jsonify({'entities': [key for key in em.models.keys()]})
    return jsonify({'entities': [name for name, val in em.models.items()]})


@app.route('/models_dynamic/')
def models_react():
    return render_template('models_dynamic.html', models=em.models)


if __name__ == '__main__':
    app.run(debug=True)
