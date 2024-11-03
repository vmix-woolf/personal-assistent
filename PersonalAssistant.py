from collections import UserDict

from numpy.ma.core import indices


class PersonalAssistant(UserDict):

    def add_record(self, contact):
        record_indices = self.data.keys()
        self.data[max(record_indices) + 1] = contact


    def find_record(self, contact_name):
        for _, record in self.data.items():
            if record.name.value == contact_name:
                return record

    def remove_record(self, contact_name):
        record_key = 0
        for key, record in self.data.items():
            if record.name.value == contact_name:
                record_key = key
        del self.data[record_key]
