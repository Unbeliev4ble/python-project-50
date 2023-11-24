from gendiff.formatters.value_foramatters import format_value_plain

POSTFIX_LENGTH = 12


def make_plain(data: dict, path=""):
    lines = []
    for key, value in data.items():
        orig_key = key[:-POSTFIX_LENGTH]
        current_value = format_value_plain(value)
        if key.endswith(' ( removed )') and f'{orig_key} (  added  )' in data:
            changed_value = format_value_plain(data[f'{orig_key} (  added  )'])
            lines.append(f"Property '{path}{orig_key}' was updated. "
                         f"From {current_value} to {changed_value}")
        elif key.endswith(' ( removed )'):
            lines.append(f"Property '{path}{orig_key}' was removed")
        elif (key.endswith(' (  added  )')
              and f'{orig_key} ( removed )' not in data):
            lines.append(f"Property '{path}{orig_key}' "
                         f"was added with value: {current_value}")
        elif isinstance(value, dict):
            current_path = path + key + '.'
            lines.append(f'{make_plain(value, current_path)}')
    return '\n'.join([line for line in lines if line])
