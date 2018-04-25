init:
	pip install pipenv
	pipenv install --dev

run:
	cd voracious; FLASK_APP=app.py pipenv run flask run

test:
	pipenv run py.test 
