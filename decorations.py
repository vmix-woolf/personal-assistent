from constants import Constants
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
    AddressIsAlreadyPresent,
    EmptyNoteException,
    NoteExceedsMaxLength
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return Constants.VALUE_ERROR.value
        except KeyError:
            return Constants.KEY_ERROR.value
        except IndexError:
            return Constants.INDEX_ERROR.value
        except PhoneNumberException:
            return Constants.PRECISE_DIGITS_ERROR.value
        except InvalidDateFormatException:
            return Constants.INVALID_FORMAT_ERROR.value
        except InvalidDateValueException:
            return Constants.INVALID_DATE_VALUE_ERROR.value
        except InvalidNameException:
            return Constants.NAME_IS_NOT_VALID.value
        except PhoneIsAlreadyBelongingException:
            return Constants.PHONE_BELONGS_TO_CONTACT.value
        except NoSuchContactException:
            return Constants.NO_SUCH_CONTACT.value
        except NoSuchPhoneNumberException:
            return Constants.NO_SUCH_PHONE_NUMBER.value
        except EmailNotValidException:
            return Constants.EMAIL_IS_NOT_VALID.value
        except EmailAlreadyPresentException:
            return Constants.EMAIL_IS_ALREADY_PRESENT.value
        except ContactHasBirthdayException:
            return Constants.CONTACT_HAS_BIRTHDAY.value
        except AddressIsAlreadyPresent:
            return Constants.ADDRESS_IS_ALREADY_PRESENT.value
        except EmptyNoteException:
            return Constants.EMPTY_NOTE.value
        except NoteExceedsMaxLength:
            return Constants.GREATER_THAN_MAX_LENGTH.value

    return inner
