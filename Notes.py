from collections import UserDict


class Notes(UserDict):

    def add_note(self, note):
        last_record_index = len(self.data)
        self.data[last_record_index + 1] = note
