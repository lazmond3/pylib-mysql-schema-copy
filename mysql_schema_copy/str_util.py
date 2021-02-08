
# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
import re


def camel_to_snake(input_str: str) -> str:
    # output = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    output = re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()
    return output

    # ref: https://stackoverflow.com/questions/19053707/converting-snake-case-to-lower-camel-case-lowercamelcase


def snake_to_camel(input_str: str) -> str:
    components = input_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def snake_to_lower_camel(input_str: str) -> str:
    r = snake_to_camel(input_str)
    return r[0].lower() + r[1:]


def snake_to_upper_camel(input_str: str) -> str:
    r = snake_to_camel(input_str)
    return r[0].upper() + r[1:]
