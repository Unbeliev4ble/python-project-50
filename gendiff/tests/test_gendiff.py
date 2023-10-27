from gendiff import generate_diff


file1 = '/home/frost/projects/file1.json'
file2 = '/home/frost/projects/file2.json'
expected_result = ("{"
                   "\n- follow: False"
                   "\n  host: hexlet.io"
                   "\n- proxy: 123.234.53.22"
                   "\n- timeout: 50"
                   "\n+ timeout: 20"
                   "\n+ verbose: True"
                   "\n}")


def test_generate_diff():
    assert generate_diff(file1, file2) == expected_result
