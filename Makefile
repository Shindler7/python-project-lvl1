# Учебный makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

