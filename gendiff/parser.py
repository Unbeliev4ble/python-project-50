import json
import yaml


def read(path):
    with open(path) as file:
        return file.read()


def get_file_format(file_name):
    return file_name.split('.')[-1]


def parse(data, orig_format) -> dict:
    if orig_format == 'json':
        return json.loads(data)
    elif orig_format in ('yaml', 'yml'):
        return yaml.safe_load(data)
