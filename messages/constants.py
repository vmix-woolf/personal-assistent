from enum import Enum

class Constants(Enum):
    NUMBER_OF_DIGITS_IN_PHONE_NUMBER = 3

    WELCOME_MESSAGE = "Welcome to the Personal Assistant bot!"
    # related to adding process
    CONTACT_ADDED = "Contact is added."
    CONTACT_UPDATED = "Contact is updated."
    CONTACT_DELETED = "Contact is deleted."
    EMAIL_ADDED = "Email is added."
    EMAIL_UPDATED = "Email is updated."
    BIRTHDAY_ADDED = "Birthday is added."
    BIRTHDAY_UPDATED = "Birthday is updated."
    ADDRESS_ADDED = "Address is added."
    NOTE_ADDED = "Note is added."

    INVALID_COMMAND_ERROR = "Invalid command."
    NOT_ENOUGH_ARGUMENTS = "Not enough arguments. Please input the correct command."
    # related to system errors
    KEY_ERROR = "This name is already in the contacts."
    VALUE_ERROR = "Enter the correct argument value."
    INDEX_ERROR = "This contact name is absent in the address book."
    # related to contacts' names
    NAME_IS_NOT_VALID = "Name is not valid."
    CONTACT_IS_ALREADY_PRESENT = "There is already such a user."
    CONTACT_LIST_EMPTY = "Contact list is empty."
    NO_SUCH_CONTACT = "No such contact in the personal assistant."
    # related to phones
    PRECISE_DIGITS_ERROR = f"Phone should consist of exactly {NUMBER_OF_DIGITS_IN_PHONE_NUMBER} digits!"
    PHONE_BELONGS_TO_CONTACT = "This phone number already belongs to this contact."
    NO_SUCH_PHONE_NUMBER = "Old phone number doesn't belong to this contact."
    # related to emails
    EMAIL_IS_NOT_VALID = "Email is not valid."
    EMAIL_IS_ALREADY_PRESENT = "Email is already present for this contact. Use 'change-email...' command."
    # related to the birthday
    INVALID_FORMAT_ERROR = "Invalid date format. Use DD.MM.YYYY"
    INVALID_DATE_VALUE_ERROR = "Invalid date value. Use correct date."
    CONTACT_HAS_BIRTHDAY = "This contact has already their birthday"
    NO_NECESSARY_TO_CONGRATULATE = "There are no contacts to be mailed in the coming days."
    TITLE_TO_CONGRATULATE = "It's necessary to congratulate the following contacts:"
    NATURAL_NUMBER_ERROR = "The number of days must be a natural number"
    # related to address
    ADDRESS_IS_ALREADY_PRESENT = "This contact has an address already. To change it please use 'change-...' command."
    # related to textbook
    EMPTY_NOTE = "You cannot create an empty note."
    GREATER_THAN_MAX_LENGTH = "Note cannot be greater than the maximum length."
    # related to file names
    ADDRESS_BOOK_FILE_PKL = 'assistant/addressbook.pkl'
    TEXTBOOK_FILE_PKL = 'assistant/textbook.pkl'
