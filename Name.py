from Field import Field


class Name(Field):
    def __init__(self, first_name, last_name=None):
        super().__init__(first_name)
        self.first_name = first_name
        self.last_name = last_name

