from collections import UserDict


class PersonalAssistant(UserDict):
    def add_record(self, contact):
        last_record_index = len(self.data)
        self.data[last_record_index + 1] = contact


    def find_record(self, contact_name):
        for _, record in self.data.items():
            if record.name.value == contact_name:
                return record
