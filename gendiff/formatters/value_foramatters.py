def format_value_plain(value):
    if not isinstance(value, dict):
        if value is None:
            result_value = 'null'
        elif isinstance(value, str):
            result_value = f"'{value}'"
        else:
            result_value = str(value).lower()
    else:
        result_value = '[complex value]'
    return result_value


def format_value_stylish(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)
