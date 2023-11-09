import json
import yaml


def get_data(file_path: str) -> dict:
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    elif file_path.endswith(('.yaml', '.yml')):
        return yaml.safe_load(open(file_path))

