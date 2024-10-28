import constants
from Exceptions import (
    PhoneNumberException,
    InvalidDateFormatException
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return constants.VALUE_ERROR
        except KeyError:
            return constants.KEY_ERROR
        except IndexError:
            return constants.INDEX_ERROR
        except PhoneNumberException:
            return constants.PRECISE_DIGITS_ERROR
        except InvalidDateFormatException:
            return constants.INVALID_FORMAT_ERROR

    return inner
