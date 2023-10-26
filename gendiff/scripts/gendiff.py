#!/usr/bin/env python3

from gendiff.cli_parse import make_cli_parse
from gendiff import generate_diff


def main():
    file1_path, file2_path = make_cli_parse()
    diff = generate_diff(file1_path, file2_path)
    print(diff)


if __name__ == '__main__':
    main()
