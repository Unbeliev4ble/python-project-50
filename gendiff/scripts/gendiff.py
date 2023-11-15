#!/usr/bin/env python3

from gendiff.cli import get_cli_args
from gendiff.gen_diff import generate_diff


def main():
    file1_path, file2_path, format = get_cli_args()
    diff = generate_diff(file1_path, file2_path, format)
    return print(diff)


if __name__ == '__main__':
    main()
