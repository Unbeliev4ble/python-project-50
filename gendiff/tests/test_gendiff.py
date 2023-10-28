import os
from gendiff import generate_diff


current_dir = os.path.dirname(os.path.abspath(__file__))

# file1_path = 'fixtures/file1.json' # относ. путь работает только в ране модуля
# file2_path = 'fixtures/file2.json'

file1_path = f'{current_dir}/fixtures/file1.json'
file2_path = f'{current_dir}/fixtures/file2.json'
expected_result = open(f'{current_dir}/fixtures/flat_json_comparing.txt').read()


# expected_result = ("{"
#                    "\n- follow: False"
#                    "\n  host: hexlet.io"
#                    "\n- proxy: 123.234.53.22"
#                    "\n- timeout: 50"
#                    "\n+ timeout: 20"
#                    "\n+ verbose: True"
#                    "\n}")
##
#
def test_generate_diff():
    assert generate_diff(file1_path, file2_path) == expected_result
