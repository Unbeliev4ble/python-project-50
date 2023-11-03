#!/usr/bin/env python3

from gendiff_app.scripts import generate_diff

file1 = './tests/fixtures/file1.yaml'
file2 = './tests/fixtures/file2.yaml'


def main():
    # file1_path, file2_path = make_cli_parse()
    diff = generate_diff.generate_diff_func(file1, file2)
    print(file1, file1)
    print(diff)


if __name__ == '__main__':
    main()
