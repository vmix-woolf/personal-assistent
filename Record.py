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


    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


    def find_phone(self, phone_number):
        try:
            index = self.phones.index(phone_number)

            return self.phones[index]
        except ValueError:
            return False


    def add_email(self, email):
        self.email = email


    def has_email(self):
        return True if self.email is not None else False


    def __str__(self):
        basic_message = f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

        if self.email is not None:
            basic_message += f", email: {self.email}"

        if self.birthday is not None:
            basic_message += f", birthday: {self.birthday}"

        return basic_message
