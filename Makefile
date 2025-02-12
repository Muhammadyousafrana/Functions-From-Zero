install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv test_*.py

lint:
	pylint --disable=R,C,E0602, wikibot.py

format:
	black *.py
all: install test lint format