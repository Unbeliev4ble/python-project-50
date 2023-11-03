install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff_app

compare:
	gendiff_app /home/frost/projects/file1.json /home/frost/projects/file2.json

test:
	cd gendiff_app/tests && poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff_app  --cov-report xml
