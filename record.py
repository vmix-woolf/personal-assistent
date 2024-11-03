from Name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

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

    def edit_email(self, new_email):
        self.email = new_email

    def add_birthday(self, birthday):
        self.birthday = birthday

    def has_birthday(self):
        return True if self.birthday is not None else False

    def edit_birthday(self, new_birthday):
        self.birthday = new_birthday

    def add_address(self, address):
        self.address = address

    def edit_address(self, new_address):
        pass

    def has_address(self):
        return True if len(self.address) != 0 else False

    def delete_city(self, name):
        pass

    def delete_street(self, name):
            pass

    def delete_building(self, name):
            pass

    def delete_apartment(self, name):
            pass

    def __str__(self):
        basic_message = f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

        if self.email is not None:
            basic_message += f", email: {self.email}"

        if self.birthday is not None:
            basic_message += f", birthday: {self.birthday}"

        if len(self.address) != 0:
            basic_message += f", address: (city: {self.address['city']}; street: {self.address['street']}; house: {self.address['building']}; apartment: {self.address['apartment']})"

        return basic_message
