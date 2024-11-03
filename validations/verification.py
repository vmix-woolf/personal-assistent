import re
import calendar

from messages.constants import Constants
from decorators.decorations import input_error


@input_error
def name_validation(name):
    return True if bool(re.match(r'[A-Za-z]{2,25}', name)) else False


@input_error
def phone_number_validation(phone_number):
    return True if phone_number.isdigit() and len(phone_number) == Constants.NUMBER_OF_DIGITS_IN_PHONE_NUMBER.value else False


@input_error
def email_validation(email):
    return True if bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email)) else False


@input_error
def birthday_format_validation(birthday):
    return True if bool(re.match(r'\d{1,2}\.\d{1,2}\.\d{4}', birthday)) else False


@input_error
def birthday_value_validation(birthday):
    day, month, year = birthday.split('.')
    day = int(day)
    month = int(month)
    year = int(year)

    if year < 1 or year > 9999:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    max_days = calendar.monthrange(year, month)[1]

    if day > max_days:
        return False

    return True
