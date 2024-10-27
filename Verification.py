import re
from datetime import datetime
from Exceptions import ExactDigitException, InvalidDateValueError, InvalidDateFormatError

class Validation:
    def __init__(self, name):
        self.name = name

def name_validation(name):
    return True if bool(re.match(r'[A-Za-z]{2,25}', name)) else False


def phone_number_validation(phone_number):
    if phone_number.isdigit() and len(phone_number) == 3:
        return True
    else:
        raise ExactDigitException

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