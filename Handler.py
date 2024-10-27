from Exceptions import (
    InvalidDateValueError,
    InvalidDateFormatError,
    ExactDigitException,
    NoSuchContact,
)
from PersonalAssistant import PersonalAssistant
from Record import Record
import re


def add_contact(args, assistant: PersonalAssistant):
    name, phone_number, *_ = args
    record = assistant.find_record(name)


    try:
        # if name is valid name then
        if name_verification(name):
            # if the number is valid phone number
            if phone_number_verification(phone_number):
                record = Record(name)
                record.add_phone(phone_number)
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


def change_contact(args, assistant: PersonalAssistant):
    pass


def show_contacts(assistant: PersonalAssistant):
    if len(assistant) == 0:
        print('There are no contacts')
    else:
        for _, contact in assistant.items():
            print(contact)


def add_email(args, assistant: PersonalAssistant):
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


def change_email(args, assistant: PersonalAssistant):
    pass

def add_address(args, assistant: PersonalAssistant):
    pass

def change_address(args, assistant: PersonalAssistant):
    pass

def add_birthday(args, assistant: PersonalAssistant):
    pass

def change_birthday(args, assistant: PersonalAssistant):
    pass


def phone_number_verification(number):
    if number.isdigit() and len(number) == 3:
        return True
    else:
        raise ExactDigitException


def name_verification(name):
    return True if bool(re.match(r'[A-Za-z]{2,25}', name)) else False


def email_verification(email):
    return True if bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email)) else False


def birthday_verification(birthday):
    if bool(re.match(r'\d{2}\.\d{2}\.\d{4}', birthday)):
        if datetime.strptime(birthday, '%d.%m.%Y'):
            return True
        else:
            raise InvalidDateValueError
    else:
        raise InvalidDateFormatError