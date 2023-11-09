from gendiff import generate_diff


FILE1_JSON_PATH = './fixtures/file1_nested.json'
FILE2_JSON_PATH = './fixtures/file2_nested.json'
FILE1_YAML_PATH = './fixtures/file1_nested.yaml'
FILE2_YAML_PATH = './fixtures/file2_nested.yaml'

EXPECTED_RESULT = open('./fixtures/comparing_nested_result.txt').read()


def test_generate_diff_json():
    assert generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH) == EXPECTED_RESULT


def test_generate_diff_yaml():
    assert generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH) == EXPECTED_RESULT


def test_generate_diff_json_yaml():
    assert generate_diff(FILE1_JSON_PATH, FILE2_YAML_PATH) == EXPECTED_RESULT
