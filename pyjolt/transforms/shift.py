from pyjolt.exceptions import PyJoltException


def shift(data: dict, spec: dict) -> dict:
    operation = spec["operation"]

    if operation != "shift":
        raise PyJoltException("Invalid operation for shift " + operation)

    transform = spec["spec"]
    result = {}
    dict_values = []

    def parse_spec(spec: dict, input_data: dict = data):
        for key, value in spec.items():
            if isinstance(value, dict):
                parse_spec(value, input_data[key])
            if isinstance(value, str):
                dict_values.append((value, input_data[key]))
            if isinstance(value, list):
                for item in value:
                    dict_values.append((item, input_data[key]))

    parse_spec(transform)

    for value, input_value in dict_values:
        if isinstance(value, str):
            parse_dict_from_str(input_value, result, value)

        elif isinstance(value, list):
            for item in value:
                parse_dict_from_str(item, result, item)

    return result


def parse_dict_from_str(input_value, result, value):
    key_list = value.split(".")
    if len(key_list) == 1:
        result[key_list[0]] = input_value
    else:
        current = result
        for key in key_list[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[key_list[-1]] = input_value
