install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv test_*.py

lint:
	pylint --disable=R,C,E0602,E1120 wikibot.py my_lib/*.py

format:
	black *.py my_lib/*.py
all: install test lint format