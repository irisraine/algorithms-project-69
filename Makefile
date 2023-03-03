install:
	poetry install

lint:
	poetry run flake8 search_engine

tests:
	poetry run pytest

coverage:
	poetry run pytest --cov=search_engine tests/ --cov-report xml
