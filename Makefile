install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

compare:
	gendiff /home/frost/projects/file1.json /home/frost/projects/file2.json

test:
	cd gendiff/tests && poetry run pytest

test-coverage:
	cd gendiff/tests
	poetry run pytest --cov=./gendiff  --cov-report xml

