import re, calendar
from datetime import datetime, date
from itertools import filterfalse

from Exceptions import (
    InvalidDateValueException,
    InvalidDateFormatException,
)
from constants import NUMBER_OF_DIGITS_IN_PHONE_NUMBER
from decorations import input_error


def name_validation(name):
    return True if bool(re.match(r'[A-Za-z]{2,25}', name)) else False


def phone_number_validation(phone_number):
    return True if phone_number.isdigit() and len(phone_number) == NUMBER_OF_DIGITS_IN_PHONE_NUMBER else False


def email_validation(email):
    return True if bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email)) else False


@input_error
def birthday_format_validation(birthday):
    return True if bool(re.match(r'\d{2}\.\d{2}\.\d{4}', birthday)) else False


@input_error
def birthday_value_validation(birthday):
    day, month, year = birthday.split('.')
    day = int(day)
    month = int(month)
    year = int(year)

    if 9999 < year < 1:
        return False
    if 12 < month < 1:
        return False

    max_days = calendar.monthrange(year, month)[1]

    if day > max_days:
        return False

    return True
