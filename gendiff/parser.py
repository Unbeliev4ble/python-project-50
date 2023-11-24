import json
import yaml


def read(path):
    with open(path) as file:
        return file.read()


def get_file_format(file_name):
    return file_name.split('.')[-1]


def parse(data, format) -> dict:
    if format == 'json':
        return json.loads(data)
    elif format in ('yaml', 'yml'):
        return yaml.safe_load(data)
