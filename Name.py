from Field import Field


class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

