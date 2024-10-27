from Name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.address = {}
        self.phones = []
        self.email = None
        self.birthday = None


    def add_phone(self, phone):
        self.phones.append(phone)


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


    def change_contact(self, name):
        pass


    def show_contacts(self):
        pass
