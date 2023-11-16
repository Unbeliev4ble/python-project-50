from gendiff import generate_diff


FILE1_JSON_PATH = './fixtures/file1_nested.json'
FILE2_JSON_PATH = './fixtures/file2_nested.json'
FILE1_YAML_PATH = './fixtures/file1_nested.yaml'
FILE2_YAML_PATH = './fixtures/file2_nested.yaml'

STYLISH_EXPECTED_RESULT = open('./fixtures/stylish_result.txt').read()
PLAIN_EXPECTED_RESULT = open('./fixtures/plain_result.txt').read()
JSON_EXPECTED_RESULT = open('./fixtures/json_result.txt').read()


def test_generate_diff_stylish():
    assert (generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH)
            == STYLISH_EXPECTED_RESULT)

    assert (generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH)
            == STYLISH_EXPECTED_RESULT)

    assert (generate_diff(FILE1_JSON_PATH, FILE2_YAML_PATH)
            == STYLISH_EXPECTED_RESULT)


def test_generate_diff_plain():
    assert (generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH, 'plain')
            == PLAIN_EXPECTED_RESULT)


def test_generate_diff_json():
    assert (generate_diff(FILE1_JSON_PATH, FILE2_YAML_PATH, 'json')
            == JSON_EXPECTED_RESULT)
