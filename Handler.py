from Record import Record
from PersonalAssistant import PersonalAssistant
from verification import (
    name_validation,
    phone_number_validation,
    email_validation,
    birthday_validation
)
from Exceptions import (
    NotEnoughArguments,
    PhoneNumberException,
    PhoneIsAlreadyBelongingException,
    NoSuchContactException,
    EmailNotValidException,
    InvalidNameException,
    EmailAlreadyPresentException,
    NoSuchPhoneNumberException
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
    try:
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
    except InvalidNameException:
        return constants.NAME_IS_NOT_VALID
    except PhoneNumberException:
        return constants.PRECISE_DIGITS_ERROR
    except PhoneIsAlreadyBelongingException:
        return constants.PHONE_BELONGS_TO_CONTACT


def change_contact(args, assistant: PersonalAssistant):
    name, old_phone_number, new_phone_number, *_ = args

    try:
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
    except NoSuchContactException:
        return constants.NO_SUCH_CONTACT
    except PhoneNumberException:
        return constants.PRECISE_DIGITS_ERROR
    except NoSuchPhoneNumberException:
        return constants.NO_SUCH_PHONE_NUMBER


@input_error
def add_email(args, assistant: PersonalAssistant):
    name, email, *_ = args

    try:
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
    except EmailNotValidException:
        return constants.EMAIL_IS_NOT_VALID
    except EmailAlreadyPresentException:
        return constants.EMAIL_IS_ALREADY_PRESENT
    except NoSuchContactException:
        return constants.NO_SUCH_CONTACT


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
    except NoSuchContactException:
        return constants.NO_SUCH_CONTACT
    except EmailNotValidException:
        return constants.EMAIL_IS_NOT_VALID


def add_address(args, assistant: PersonalAssistant):
    pass


def change_address(args, assistant: PersonalAssistant):
    pass


def add_birthday(args, assistant: PersonalAssistant):
    pass


def change_birthday(args, assistant: PersonalAssistant):
    pass
