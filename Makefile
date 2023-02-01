pip-install-poetry:
		pip install poetry

poetry-config:
		poetry config virtualenvs.create false
		poetry install --no-root

flake:
	flake8 -v ./

isort: 
		isort .

black:
		black *.py

bandit:
		bandit -r .

linters:
		make isort
		make bandit
		make black

tests:
		coverage run manage.py test

bumpversion:
	bumpversion --message '[skip ci] Bump version: {current_version} → {new_version}' --list --verbose $(part)
	