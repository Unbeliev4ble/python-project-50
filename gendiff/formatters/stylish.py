import itertools
from gendiff.formatters.value_foramatters import format_value_stylish


PREFIXES = ('+ ', '- ', '  ')
PREFIX_LENGTH = 2


def make_stylish(dict_to_style, replacer=' ', spaces_count=4):

    def walk(data, depth=0):
        if not isinstance(data, dict):
            return format_value_stylish(data)
        indent_size = depth + spaces_count
        indent = replacer * indent_size
        ident_for_changed = replacer * (indent_size - PREFIX_LENGTH)
        bracket_indent = replacer * depth
        lines = []
        for k, v in data.items():
            if k.startswith(PREFIXES):
                lines.append(f'{ident_for_changed}{k}: {walk(v, indent_size)}')
            else:
                lines.append(f'{indent}{k}: {walk(v, indent_size)}')
        result = itertools.chain("{", lines, [bracket_indent + "}"])
        return '\n'.join(result)
    return walk(dict_to_style, 0)
