from Field import Field


class Note(Field):

    def __init__(self, note):
        super().__init__(note)
        self.note = note
