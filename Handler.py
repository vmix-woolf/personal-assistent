from Record import Record
from PersonalAssistant import PersonalAssistant
from Verification import (
    name_validation,
    phone_number_validation,
    email_validation, Verification
)
from Exceptions import (
    PhoneNumberException,
    ContactAlreadyPresentException,
    NoSuchContactException,
    EmailNotValidException,
    InvalidNameException,
    EmailAlreadyPresentException
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
    record = assistant.find_record(name)
    # try:
    #     if record is None:  # there's no such record yet.
    #         if not name_validation(name):
    #             raise InvalidNameException
    #
    #         if not phone_number_validation(phone_number):
    #             raise PhoneNumberException
    #
    #         record = Record(name)
    #         assistant.add_record(record)
    #         record.add_phone(phone_number)
    #
    #         return constants.CONTACT_ADDED
    #     else:  # such a record already exists
    #         if not phone_number_validation(phone_number):
    #             raise PhoneNumberException
    #
    #         if record.find_phone(phone_number):
    #             return constants.PHONE_IS_IN_BOOK
    #         else:
    #             record.add_phone(phone_number)
    #             return constants.CONTACT_UPDATED
    # except InvalidNameException:
    #     return constants.NAME_IS_NOT_VALID
    # except PhoneNumberException:
    #     return constants.PRECISE_DIGITS_ERROR
    # except ContactAlreadyPresentException:
    #     return constants.CONTACT_IS_ALREADY_PRESENT

    if record is None:  # if such name is new
        if phone_number_validation(phone_number):
            record = Record(name)
            assistant.add_record(record)
            record.add_phone(phone_number)

            return constants.CONTACT_ADDED
        else:
            raise PhoneNumberException()
    else:  # continue if such name is already kept
        if record.find_phone(phone_number):
            return constants.PHONE_IS_IN_BOOK
        else:
            record.add_phone(phone_number)

            return constants.CONTACT_UPDATED


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
            return constants.EMAIL_IS_ADDED
        else:
            raise EmailNotValidException
    except EmailNotValidException:
        return constants.EMAIL_IS_NOT_VALID
    except EmailAlreadyPresentException:
        return constants.EMAIL_IS_ALREADY_PRESENT
    except NoSuchContactException:
        return constants.NO_SUCH_CONTACT

def change_contact(args, assistant: PersonalAssistant):
    pass

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

