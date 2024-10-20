class Tree:

    def __init__(self, data: dict):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, item, value):
        self.data[item] = value
