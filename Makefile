run:
	FLASK_APP=voracious/app.py pipenv run flask run

test:
	pipenv run py.test tests
