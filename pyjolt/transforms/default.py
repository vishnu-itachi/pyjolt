from pyjolt.exceptions import PyJoltException


def default(data: dict, spec: dict) -> dict:
    operation = spec["operation"]

    if operation != "default":
        raise PyJoltException(f"Invalid operation for default: {operation}")

    transform = spec["spec"]

    def add_default(data: dict, spec: dict) -> dict:
        for key, value in spec.items():
            if isinstance(value, dict):
                add_default(data[key], value)
            elif isinstance(value, str):
                data[key] = value
            else:
                raise PyJoltException(f"check add_default: {value}")
        return data

    return add_default(data, transform)
