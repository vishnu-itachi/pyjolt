class Spec:
    def __init__(self, spec: dict):
        self.spec = spec
        self.transforms = {}
        self._parse_spec()

    def _parse_spec(self):
        for transform in self.spec:
            self.transforms[transform["operation"]] = transform["spec"]
