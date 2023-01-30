pip-install-poetry:
		pip install poetry

poetry-config:
		poetry config virtualenvs.create false
		poetry install --no-root

linters:
		black *.py
		isort .
		bandit -r .

tests:
		coverage run manage.py test