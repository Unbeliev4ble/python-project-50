from gendiff import generate_diff
from gendiff.get_data import get_data
# from gendiff.get_diff import get_diff
import os


def get_path(file_name: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read_file(path: str):
    return open(path).read()


FILE1_JSON_PATH = get_path('file1_nested.json')
FILE2_JSON_PATH = get_path('file2_nested.json')
FILE1_YAML_PATH = get_path('file1_nested.yaml')
FILE2_YAML_PATH = get_path('file2_nested.yaml')


STYLISH_EXPECTED_RESULT = read_file(get_path('stylish_result.txt'))
PLAIN_EXPECTED_RESULT = read_file(get_path('plain_result.txt'))
JSON_EXPECTED_RESULT = read_file(get_path('json_result.txt'))


def test_get_data():
    assert get_data(FILE1_JSON_PATH) == {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {'key': 'value', 'doge': {
                'wow': ''}}},
        'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
        'group2': {'abc': 12345, 'deep': {'id': 45}}
    }

    assert get_data(FILE2_YAML_PATH) == {
        'common': {
            'follow': False,
            'setting1': 'Value 1',
            'setting3': None,
            'setting4': 'blah blah',
            'setting5': {'key5': 'value5'},
            'setting6': {
                'key': 'value',
                'ops': 'vops',
                'doge': {'wow': 'so much'}}},
        'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'},
        'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}
    }


def test_generate_diff():

    json_files_stylish = generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH)
    yaml_files_stylish = generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH)
    json_files_plain = generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH, 'plain')
    yaml_files_plain = generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH, 'plain')
    json_files_json = generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH, 'json')
    yaml_files_json = generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH, 'json')

    assert json_files_stylish == STYLISH_EXPECTED_RESULT
    assert yaml_files_stylish == STYLISH_EXPECTED_RESULT
    assert yaml_files_plain == PLAIN_EXPECTED_RESULT
    assert json_files_plain == PLAIN_EXPECTED_RESULT
    assert json_files_json == JSON_EXPECTED_RESULT
    assert yaml_files_json == JSON_EXPECTED_RESULT
