import json


def generate_diff(file1_path, file2_path):
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
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


# file1 = '/home/frost/projects/file1.json'
# file2 = '/home/frost/projects/file2.json'
# print(generate_diff(file1, file2))
