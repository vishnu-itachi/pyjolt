from pyjolt.exceptions import PyJoltException


def cardinality(data: dict, spec: dict) -> dict:
    operation = spec["operation"]

    if operation != "cardinality":
        raise PyJoltException(f"Invalid operation for cardinality: {operation}")

    spec = spec["spec"]

    def _cardinality(data: dict, spec: dict) -> dict:
        for key, value in spec.items():
            if isinstance(value, dict):
                _cardinality(data[key], value)
            elif isinstance(value, str):
                if value not in ["ONE", "MANY"]:
                    raise PyJoltException(
                        "The value of cardinality must be " "ONE or MANY"
                    )
                if value == "MANY":
                    data[key] = [data[key]]
                else:
                    if len(data[key]) > 1:
                        data[key] = data[key][0]
                    else:
                        data[key] = data[key][0]

            else:
                raise PyJoltException(f"check _cardinality: {value}")

        return data

    return _cardinality(data, spec)
