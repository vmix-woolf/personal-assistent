from Name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None


    def add_phone(self, phone):
        self.phones.append(phone)


    def add_email(self, email):
        self.email = email


    def __str__(self):
        basic_message = f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

        if self.email is not None:
            basic_message += f", email: {self.email}"

        if self.birthday is not None:
            basic_message += f", birthday: {self.birthday}"

        return basic_message


    def change_contact(self, name):
        pass


    def show_contacts(self):
        pass
