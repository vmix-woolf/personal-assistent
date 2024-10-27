from Record import Record
from PersonalAssistant import PersonalAssistant
from Verification import (
    name_validation,
    phone_number_validation
)
from Exceptions import (
    ExactDigitException,
    NoSuchContact
)


class Handler:
    def __init__(self):
        self.phone_number = None
        self.name = None

    def add_contact(self, args, assistant):
        self.name, self.phone_number, *_ = args
        # record = assistant.find_record(self.name)

        try:
            # if name is valid name then
            # if name_verification(self.name):
            if name_validation(self.name):
                # if the number is valid phone number
                if phone_number_validation(self.phone_number):
                    record = Record(self.name)
                    record.add_phone(self.phone_number)
                    assistant.add_record(record)
                    print(f"Contact added.")
                else:
                    raise ExactDigitException
            # if first_param is not valid name then value error exception
            else:
                raise ValueError
        except ExactDigitException:
            print(f"Phone should consist of exactly 3 digits!")
        except ValueError:
            print(f"Please input correct contact name")

    def change_contact(self, args, assistant: PersonalAssistant):
        pass

    def show_contacts(self, assistant: PersonalAssistant):
        if len(assistant) == 0:
            print('There are no contacts')
        else:
            for _, contact in assistant.items():
                print(contact)

    def add_email(self, args, assistant: PersonalAssistant):
        name, email, *_ = args
        if email_verification(email):
            record = assistant.find_record(name)

            try:
                if record is not None:
                    record.add_email(email)
                    print(f"Email added.")
                else:
                    raise NoSuchContact
            except NoSuchContact:
                print(f"No such contact - {name}")

    def change_email(self, args, assistant: PersonalAssistant):
        pass

    def add_address(self, args, assistant: PersonalAssistant):
        pass

    def change_address(self, args, assistant: PersonalAssistant):
        pass

    def add_birthday(self, args, assistant: PersonalAssistant):
        pass

    def change_birthday(self, args, assistant: PersonalAssistant):
        pass

