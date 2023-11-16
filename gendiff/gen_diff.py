from gendiff.get_diff import get_diff
from gendiff.get_data import get_data
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json_ import make_json


def generate_diff(file1_path, file2_path, format='stylish'):
    dict1 = get_data(file1_path)
    dict2 = get_data(file2_path)
    diff_dict = get_diff(dict1, dict2)
    if format == 'stylish':
        return make_stylish(diff_dict)
    elif format == 'plain':
        return make_plain(diff_dict)
    elif format == 'json':
        return make_json(diff_dict)

# print(generate_diff('./tests/fixtures/HEX1Y.yml',
# './tests/fixtures/HEX1Y.yml', 'plain'))
# d1 = (get_data('./tests/fixtures/HEX1Y.yml'))
# d2 = (get_data('./tests/fixtures/HEX2Y.yml'))
# d = (get_diff(d1, d2))
#
# print(make_plain(d))
