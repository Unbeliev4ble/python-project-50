import itertools
from gendiff.formatters.value_foramatters import format_value_stylish

POSTFIXES = {" (unchanged)": "  ",
             " ( removed )": "- ",
             " (  added  )": "+ ",
             }
POSTFIX_LENGTH = 12
PREFIX_LENGTH = 2


def style_key(key: str):
    postfix = key[-POSTFIX_LENGTH:]
    prefix = POSTFIXES[postfix]
    orig_key = key[:-POSTFIX_LENGTH]
    new_key = f'{prefix}{orig_key}'
    return new_key


def make_stylish(dict_to_style: dict, replacer=' ', spaces_count=4):
    def walk(data, depth=0):
        if not isinstance(data, dict):
            return format_value_stylish(data)
        indent_size = depth + spaces_count
        indent = replacer * indent_size
        ident_for_changed = replacer * (indent_size - PREFIX_LENGTH)
        bracket_indent = replacer * depth
        lines = []
        for k, v in data.items():
            if k.endswith(tuple(POSTFIXES)):
                lines.append(f'{ident_for_changed}'
                             f'{style_key(k)}: {walk(v, indent_size)}')
            else:
                lines.append(f'{indent}{k}: {walk(v, indent_size)}')
        result = itertools.chain("{", lines, [bracket_indent + "}"])
        return '\n'.join(result)

    return walk(dict_to_style, 0)
