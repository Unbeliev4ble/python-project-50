import json


def make_json(data: dict):
    return json.dumps(data, indent=4)
