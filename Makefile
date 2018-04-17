run:
	cd voracious; FLASK_APP=app.py pipenv run flask run

test:
	pipenv run py.test 
