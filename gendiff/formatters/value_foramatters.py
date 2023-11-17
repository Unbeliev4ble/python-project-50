def format_value_plain(value):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        elif isinstance(value, str):
            return f"'{value}'"
        else:
            return str(value).lower()
    else:
        return '[complex value]'


def format_value_stylish(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)
