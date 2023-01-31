pip-install-poetry:
		pip install poetry

poetry-config:
		poetry config virtualenvs.create false
		poetry install --no-root

flake:
		flake8 -v .

isort:
		isort .

bandit:
		bandit -r .

black:
		black --check --line-length 120 --exclude "/(\.eggs|\.git|\.hg|\.mypy _cache|\.nox|\.tox|\.venv|_build|buck- out|build|dist|migrations|node_modules)/" ./

linters:
		make flake
		make isort
		make bandit
		make black

tests:
		coverage run manage.py test

bumpversion:
		 bumpversion --message '[skip ci] Bump version: {current_version} → {new_version}' --list --verbose $(part)

