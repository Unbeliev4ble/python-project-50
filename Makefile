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
	poetry run gendiff /home/frost/projects/python-project-50/gendiff/tests/fixtures/file1_nested.json /home/frost/projects/python-project-50/gendiff/tests/fixtures/file2_nested.json

compare-plain:
	poetry run gendiff -f json /home/frost/projects/python-project-50/gendiff/tests/fixtures/file1_nested.json /home/frost/projects/python-project-50/gendiff/tests/fixtures/file2_nested.json

test:
	cd gendiff/tests && poetry run pytest

test-coverage:
	cd gendiff/tests &&	poetry run pytest --cov=gendiff  --cov-report xml

hexy:
	poetry run gendiff -f plain /home/frost/PycharmProjects/HEXS/file1.yml /home/frost/PycharmProjects/HEXS/file2.yml



