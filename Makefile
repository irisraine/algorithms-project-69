install:
	poetry install

lint:
	poetry run flake8 search_engine

tests:
	poetry run pytest
