import pickle

from textbook.notes import Notes
from assistant.addressbook import PersonalAssistant
from handlers.command_parser import parse_input
from messages.constants import Constants
from handlers.handler import (
    show_contacts,
    add_contact,
    change_contact,
    remove_contact,
    add_email,
    change_email,
    add_address,
    change_address,
    remove_city,
    remove_street,
    remove_building,
    remove_apartment,
    add_birthday,
    change_birthday,
    showcase_contact,
    add_note,
    show_notes,
    birthdays
)


def main():
    assistant = load_data(Constants.ADDRESS_BOOK_FILE_PKL.value, PersonalAssistant)
    notes = load_data(Constants.TEXTBOOK_FILE_PKL.value, Notes)
    print(Constants.WELCOME_MESSAGE.value)

    command_functions = {
        "add": lambda arguments: add_contact(arguments, assistant),
        "change": lambda arguments: change_contact(arguments, assistant),
        "remove": lambda arguments: remove_contact(arguments, assistant),
        "showcase": lambda arguments: showcase_contact(arguments, assistant),
        "add-email": lambda arguments: add_email(arguments, assistant),
        "change-email": lambda arguments: change_email(arguments, assistant),
        "add-address": lambda arguments: add_address(arguments, assistant),
        "change-address": lambda arguments: change_address(args, assistant),
        "remove-city": lambda arguments: remove_city(arguments, assistant),
        "remove-street": lambda arguments: remove_street(arguments, assistant),
        "remove-building": lambda arguments: remove_building(arguments, assistant),
        "remove-apartment": lambda arguments: remove_apartment(arguments, assistant),
        "add-birthday": lambda arguments: add_birthday(arguments, assistant),
        "change-birthday": lambda arguments: change_birthday(arguments, assistant),
        "birthdays": lambda arguments: birthdays(arguments, assistant),
        "add-note": lambda _: add_note(notes),
        "all-textbook": lambda _: show_notes(notes),
        "all": lambda _: show_contacts(assistant),
    }

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            save_data(Constants.ADDRESS_BOOK_FILE_PKL.value, assistant)
            save_data(Constants.TEXTBOOK_FILE_PKL.value, notes)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in command_functions:
            print(command_functions[command](args))
        else:
            print(Constants.INVALID_COMMAND_ERROR.value)


def save_data(filename, data):
    try:
        with open(filename, "wb") as fh:
            pickle.dump(data, fh)
    except Exception as e:
        print(f"Error saving data: {e}")


def load_data(filename, default_class):
    try:
        with open(filename, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        return default_class()
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        return default_class()


if __name__ == "__main__":
    main()