#!/usr/bin/env python3

from gendiff.cli_parse import make_cli_parse
from gendiff.gen_diff import generate_diff


def main():
    file1_path, file2_path, format = make_cli_parse()
    diff = generate_diff(file1_path, file2_path, format)
    return print(diff)


if __name__ == '__main__':
    main()
