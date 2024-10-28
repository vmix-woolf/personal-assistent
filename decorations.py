import constants
from Exceptions import (
    PhoneNumberException,
    InvalidDateFormatException,
    InvalidDateValueException,
    InvalidNameException,
    PhoneIsAlreadyBelongingException,
    NoSuchContactException,
    NoSuchPhoneNumberException,
    EmailNotValidException,
    EmailAlreadyPresentException,
    ContactHasBirthdayException,
    AddressIsAlreadyPresent
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
        except InvalidDateValueException:
            return constants.INVALID_DATE_VALUE_ERROR
        except InvalidNameException:
            return constants.NAME_IS_NOT_VALID
        except PhoneIsAlreadyBelongingException:
            return constants.PHONE_BELONGS_TO_CONTACT
        except NoSuchContactException:
            return constants.NO_SUCH_CONTACT
        except NoSuchPhoneNumberException:
            return constants.NO_SUCH_PHONE_NUMBER
        except EmailNotValidException:
            return constants.EMAIL_IS_NOT_VALID
        except EmailAlreadyPresentException:
            return constants.EMAIL_IS_ALREADY_PRESENT
        except ContactHasBirthdayException:
            return constants.CONTACT_HAS_BIRTHDAY
        except AddressIsAlreadyPresent:
            return constants.ADDRESS_IS_ALREADY_PRESENT

    return inner
