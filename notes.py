from collections import UserDict


class Notes(UserDict):

    def add_note(self, note):
        notes_indices = self.data.keys()

        if len(notes_indices) == 0:
            self.data[0] = note
        else:
            self.data[max(notes_indices) + 1] = note
