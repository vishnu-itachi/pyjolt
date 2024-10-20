from pyjolt.exceptions import PyJoltException


def remove(data: dict, spec: dict) -> dict:

    operation = spec["operation"]

    if operation != "remove":
        raise PyJoltException(f"Invalid operation for remove: {operation}")

    transform = spec["spec"]

    def _remove(data: dict, spec: dict) -> dict:
        for key, value in spec.items():
            if isinstance(value, dict):
                _remove(data[key], value)
            elif isinstance(value, str):
                if value != "":
                    raise PyJoltException("The value of remove must be " "")
                del data[key]
            else:
                PyJoltException(f"check _remove: {value}")

        return data

    return _remove(data, transform)
