import re
from datetime import datetime
from Exceptions import (
    InvalidDateValueException,
    InvalidDateFormatException,
)
from constants import NUMBER_OF_DIGITS_IN_PHONE_NUMBER


class Verification:
    def __init__(self, name):
        self.name = name

def name_validation(name):
    return True if bool(re.match(r'[A-Za-z]{2,25}', name)) else False


def phone_number_validation(phone_number):
    # TODO: consider not throwing an exception and return False with ternary operator - done
    return True if phone_number.isdigit() and len(phone_number) == NUMBER_OF_DIGITS_IN_PHONE_NUMBER else False


def email_validation(email):
    return True if bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email)) else False


def birthday_validation(birthday):
    if bool(re.match(r'\d{2}\.\d{2}\.\d{4}', birthday)):
        try:
            datetime.strptime(birthday, '%d.%m.%Y')
            return True
        except ValueError:
            raise InvalidDateValueException
    else:
        raise InvalidDateFormatException
