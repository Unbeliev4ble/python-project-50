from gendiff.get_diff import get_diff
from gendiff.parser import parse, get_file_format, read
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json_ import make_json


def generate_diff(file1_path, file2_path, format='stylish'):
    dict1 = parse(read(file1_path), get_file_format(file1_path))
    dict2 = parse(read(file2_path), get_file_format(file2_path))
    diff_dict = get_diff(dict1, dict2)
    if format == 'stylish':
        return make_stylish(diff_dict)
    elif format == 'plain':
        return make_plain(diff_dict)
    elif format == 'json':
        return make_json(diff_dict)
