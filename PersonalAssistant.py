from collections import UserDict


class PersonalAssistant(UserDict):
    current_id = 1

    def add_record(self, record):
        self.data[PersonalAssistant.current_id] = record
        PersonalAssistant.current_id += 1

    def find_record(self, user_name):
        for _, record in self.data.items():
            if record.name.value == user_name:
                return record
