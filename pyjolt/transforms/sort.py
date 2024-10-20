from pyjolt.exceptions import PyJoltException


def sort(data: dict, spec: dict) -> dict:
    operation = spec["operation"]

    if operation != "sort":
        raise PyJoltException(f"Invalid operation for sort: {operation}")

    def sort_dict_recursively(data: dict) -> dict:
        if not isinstance(data, dict):
            return data
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = {
                    k: sort_dict_recursively(v) for k, v in sorted(value.items())
                }
            elif isinstance(value, list):
                data[key] = [sort_dict_recursively(i) for i in sorted(value)]
            else:
                raise PyJoltException(f"check sort_dict_recursively: {value}")

        return data

    return sort_dict_recursively(data)
