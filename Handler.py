from Record import Record
from PersonalAssistant import PersonalAssistant
from verification import (
    name_validation,
    phone_number_validation,
    email_validation,
    birthday_format_validation,
    birthday_value_validation
)
from Exceptions import (
    PhoneNumberException,
    PhoneIsAlreadyBelongingException,
    NoSuchContactException,
    EmailNotValidException,
    InvalidNameException,
    EmailAlreadyPresentException,
    NoSuchPhoneNumberException,
    InvalidDateFormatException,
    InvalidDateValueException,
    ContactHasBirthdayException,
    NoBirthdayException,
    AddressIsAlreadyPresent
)
from decorations import input_error
import constants


@input_error
def show_contacts(assistant: PersonalAssistant):
    if len(assistant) == 0:
        print('There are no contacts')
    else:
        for _, contact in assistant.items():
            print(contact)


@input_error
def add_contact(args, assistant):
    name, phone_number, *_ = args

    if len(args) < 2:
        raise ValueError

    if not name_validation(name):
        raise InvalidNameException

    if not phone_number_validation(phone_number):
        raise PhoneNumberException

    record = assistant.find_record(name)

    if record is None:  # if such name is new
        record = Record(name)
        assistant.add_record(record)
        record.add_phone(phone_number)

        return constants.CONTACT_ADDED
    elif record.find_phone(phone_number):  # continue if such name is already kept
        raise PhoneIsAlreadyBelongingException
    else:
        record.add_phone(phone_number)
        return constants.CONTACT_UPDATED


@input_error
def change_contact(args, assistant: PersonalAssistant):
    name, old_phone_number, new_phone_number, *_ = args

    record = assistant.find_record(name)

    if record is None:
        raise NoSuchContactException

    if not phone_number_validation(new_phone_number):
        raise PhoneNumberException

    if record.find_phone(old_phone_number):
        record.edit_phone(old_phone_number, new_phone_number)
    else:
        raise NoSuchPhoneNumberException

    return constants.CONTACT_UPDATED


@input_error
def add_email(args, assistant: PersonalAssistant):
    name, email, *_ = args

    record = assistant.find_record(name)

    if record is None:
        raise NoSuchContactException

    if record.has_email():
        raise EmailAlreadyPresentException

    if email_validation(email):
        record.add_email(email)

        return constants.EMAIL_ADDED
    else:
        raise EmailNotValidException


@input_error
def change_email(args, assistant: PersonalAssistant):
    try:
        name, new_email, *_ = args

        if len(args) < 2:
            raise ValueError

        record = assistant.find_record(name)

        if record is None:
            raise NoSuchContactException

        if not email_validation(new_email):
            raise EmailNotValidException

        record.edit_email(new_email)

        return constants.EMAIL_UPDATED
    except ValueError:
        return constants.NOT_ENOUGH_ARGUMENTS


@input_error
def add_address(args, assistant: PersonalAssistant):
    name, *_ = args

    if len(args) < 1:
        raise ValueError

    record = assistant.find_record(name)

    if record is None:
        raise NoSuchContactException

    if record.has_address():
        raise AddressIsAlreadyPresent
    else:
        city = input('Type the name of the city: ')
        street = input('Type the name of the street: ')
        building = input('Type a number of the building: ')
        apartment = int(input('Type a number of the apartment: '))
        address = {
            'city': city,
            'street': street,
            'building': building,
            'apartment': apartment
        }

        record.add_address(address)

        return constants.ADDRESS_ADDED


def change_address(args, assistant: PersonalAssistant):
    pass


@input_error
def add_birthday(args, assistant: PersonalAssistant):
    name, birthday, *_ = args

    if len(args) < 2:
        raise ValueError

    if not name_validation(name):
        raise InvalidNameException

    record = assistant.find_record(name)

    if record is None:
        raise NoSuchContactException

    if record.has_birthday():
        raise ContactHasBirthdayException

    if not birthday_format_validation(birthday):
        raise InvalidDateFormatException

    if not birthday_value_validation(birthday):
        raise InvalidDateValueException('Incorrect date')
    else:
        record.add_birthday(birthday)

        return constants.BIRTHDAY_ADDED


def change_birthday(args, assistant: PersonalAssistant):
    name, new_birthday, *_ = args

    if len(args) < 2:
        raise ValueError

    if not name_validation(name):
        raise InvalidNameException

    record = assistant.find_record(name)

    if record is None:
        raise NoSuchContactException

    if not record.has_birthday():
        raise NoBirthdayException

    if not birthday_format_validation(new_birthday):
        raise InvalidDateFormatException

    if not birthday_value_validation(new_birthday):
        raise InvalidDateValueException('Incorrect date')
    else:
        record.edit_birthday(new_birthday)

        return constants.BIRTHDAY_UPDATED