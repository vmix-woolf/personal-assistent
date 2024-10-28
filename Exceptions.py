class NotEnoughArguments(Exception):
    pass

class InvalidDateFormatException(Exception):
    pass

class InvalidDateValueException(ValueError):
    pass

class PhoneNumberException(Exception):
    pass

class NoSuchPhoneNumberException(Exception):
    pass

class InvalidNameException(Exception):
    pass

class EmailNotValidException(Exception):
    pass

class NoSuchContactException(Exception):
    pass

class EmailAlreadyPresentException(Exception):
    pass

class PhoneIsAlreadyBelongingException(Exception):
    pass