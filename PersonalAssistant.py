from collections import UserDict


class PersonalAssistant(UserDict):
    current_id = 1

    def add_record(self, record):
        self.data[PersonalAssistant.current_id] = record
        PersonalAssistant.current_id += 1
