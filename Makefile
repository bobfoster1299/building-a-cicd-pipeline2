setup:
	python3 -m venv ~/.udacity-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pylint --disable=R,C,W1203,W0702,E0611 app.py

all: install test