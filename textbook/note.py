from assistant.field import Field


class Note(Field):

    def __init__(self, note):
        super().__init__(note)
        self.note = note

    def __str__(self):
        basic_message = f"{self.note}"

        return basic_message
