import json


def get_data(file_path: str) -> dict:
    return json.load(open(file_path))


def generate_diff(file1_path: str, file2_path: str) -> str:

    file1 = get_data(file1_path)
    file2 = get_data(file2_path)

    diff_string = '{\n'
    for key in sorted(file1 | file2):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff_string += f'  {key}: {file1[key]}'
            else:
                diff_string += f'- {key}: {file1[key]}' + '\n'
                diff_string += f'+ {key}: {file2[key]}'

        elif key in file1:
            diff_string += f'- {key}: {file1[key]}'

        elif key in file2:
            diff_string += f'+ {key}: {file2[key]}'
        diff_string += '\n'
    diff_string += '}'
    return diff_string

# file1 = 'tests/fixtures/file1.json'   # проверка
# file2 = 'tests/fixtures/file2.json'
