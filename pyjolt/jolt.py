from pyjolt.exceptions import PyJoltException
from pyjolt.transforms.cardinality import cardinality
from pyjolt.transforms.default import default
from pyjolt.transforms.remove import remove
from pyjolt.transforms.shift import shift
from pyjolt.transforms.sort import sort


class Jolt:
    def __init__(self, data: dict):
        self.data = data

    def shift(self, spec: dict) -> "Jolt":
        self.data = shift(self.data, spec)
        return self

    def transform(self, spec: dict):
        transforms = {item["operation"]: item for item in spec}

        for transform in transforms:
            match transform:
                case "shift":
                    self.data = shift(self.data, transforms[transform])
                case "default":
                    self.data = default(self.data, transforms[transform])
                case "remove":
                    self.data = remove(self.data, transforms[transform])
                case "sort":
                    self.data = sort(self.data, transforms[transform])
                case "cardinality":
                    self.data = cardinality(self.data, transforms[transform])
                case _:
                    raise PyJoltException(
                        "Invalid operation for transform " + transform
                    )
