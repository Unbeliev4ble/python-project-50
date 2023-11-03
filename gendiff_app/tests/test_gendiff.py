import os
from gendiff_app.scripts.generate_diff import generate_diff_func


current_dir = os.path.dirname(os.path.abspath(__file__))


file1_path_json = f'{current_dir}/fixtures/file1.json'
file2_path_json = f'{current_dir}/fixtures/file2.json'
file1_path_yaml = f'{current_dir}/fixtures/file1.yaml'
file2_path_yaml = f'{current_dir}/fixtures/file2.yaml'

expected_result = open(f'{current_dir}/fixtures/comparing_result.txt').read()


def test_generate_diff_json():
    assert generate_diff_func(file1_path_json, file2_path_json) == expected_result


def test_generate_diff_yaml():
    assert generate_diff_func(file1_path_yaml, file2_path_yaml) == expected_result
