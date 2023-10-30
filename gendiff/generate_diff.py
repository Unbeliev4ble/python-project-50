from gendiff import parse_files


def generate_diff(file1_path: str, file2_path: str) -> str:

    data1 = parse_files.get_data(file1_path)
    data2 = parse_files.get_data(file2_path)

    diff_string = '{\n'
    for key in sorted(data1 | data2):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_string += f'  {key}: {data1[key]}'
            else:
                diff_string += f'- {key}: {data1[key]}' + '\n'
                diff_string += f'+ {key}: {data2[key]}'

        elif key in data1:
            diff_string += f'- {key}: {data1[key]}'

        elif key in data2:
            diff_string += f'+ {key}: {data2[key]}'
        diff_string += '\n'
    diff_string += '}'
    return diff_string

# file1 = 'tests/fixtures/file1.json'   # проверка json
# file2 = 'tests/fixtures/file2.json'
# # #
# file1 = 'tests/fixtures/file1.yaml'   # проверка yaml
# file2 = 'tests/fixtures/file2.yaml'
# # # #
# print(generate_diff(file1, file2))
