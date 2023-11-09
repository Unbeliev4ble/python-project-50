def get_diff(data1: dict, data2: dict) -> dict: # noqa
    diff_dict = {}
    united_data = sorted(data1 | data2)
    for key in united_data:
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff_dict[f'  {key}'] = data1[key]
        elif key not in data2:
            diff_dict[f'- {key}'] = data1[key]
        elif key not in data1:
            diff_dict[f'+ {key}'] = data2[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff_dict[key] = get_diff(data1[key], data2[key])
        elif data1[key] != data2[key]:
            diff_dict[f'- {key}'] = data1[key]
            diff_dict[f'+ {key}'] = data2[key]
    return diff_dict


