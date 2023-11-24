from gendiff import generate_diff
from gendiff.parser import read
import pytest
import os


def get_path(file_name: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


FILE1_JSON_PATH = get_path('file1_nested.json')
FILE2_JSON_PATH = get_path('file2_nested.json')
FILE1_YAML_PATH = get_path('file1_nested.yaml')
FILE2_YAML_PATH = get_path('file2_nested.yaml')

STYLISH_EXPECTED_RESULT = read(get_path('stylish_result.txt'))
PLAIN_EXPECTED_RESULT = read(get_path('plain_result.txt'))
JSON_EXPECTED_RESULT = read(get_path('json_result.txt'))


@pytest.mark.parametrize('gen_diff, result',
                         [
                             (generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH), STYLISH_EXPECTED_RESULT),
                             (generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH), STYLISH_EXPECTED_RESULT),
                             (generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH, 'plain'), PLAIN_EXPECTED_RESULT),
                             (generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH, 'plain'), PLAIN_EXPECTED_RESULT),
                             (generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH, 'json'), JSON_EXPECTED_RESULT),
                             (generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH, 'json'), JSON_EXPECTED_RESULT),
                         ])
def test_generation_diff(gen_diff, result):
    assert gen_diff == result
