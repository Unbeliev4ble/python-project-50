from gendiff.formatters.value_foramatters import format_value_plain

PREFIX_LENGTH = 2


def make_plain(data: dict, path=""):
    lines = []
    for key, value in data.items():
        orig_key = key[PREFIX_LENGTH:]
        current_value = format_value_plain(value)
        if key.startswith('- ') and f'+ {orig_key}' in data:
            changed_value = format_value_plain(data[f'+ {orig_key}'])
            lines.append(f"Property '{path}{orig_key}' was updated. "
                         f"From {current_value} to {changed_value}")
        elif key.startswith('- '):
            lines.append(f"Property '{path}{orig_key}' was removed")
        elif key.startswith('+ ') and f'- {orig_key}' not in data:
            lines.append(f"Property '{path}{orig_key}' "
                         f"was added with value: {current_value}")
        elif isinstance(value, dict):
            current_path = path + key + '.'
            lines.append(f'{make_plain(value, current_path)}')
    return '\n'.join([line for line in lines if line])
