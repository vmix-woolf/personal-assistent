import pickle

from personal_assistant import PersonalAssistant
from notes import Notes
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
    show_notes
)


def main():

    assistant = load_data_address_book(filename=Constants.ADDRESS_BOOK_FILE_PKL.value)
    notes = load_data_notes(filename=Constants.NOTES_FILE_PKL.value)
    print(Constants.WELCOME_MESSAGE.value)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            save_data_address_book(assistant, Constants.ADDRESS_BOOK_FILE_PKL.value)
            save_data_notes(notes, Constants.NOTES_FILE_PKL.value)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, assistant))
        elif command == "change":
            print(change_contact(args, assistant))
        elif command == "remove":
            print(remove_contact(args, assistant))
        elif command == "showcase":
            print(showcase_contact(args, assistant))
        elif command == "add-email":
            print(add_email(args, assistant))
        elif command == "change-email":
            print(change_email(args, assistant))
        elif command == "add-address":
            print(add_address(args, assistant))
        elif command == "change-address":
            print(change_address(args, assistant))
        elif command == "remove-city":
            print(remove_city(args, assistant))
        elif command == "remove-street":
            print(remove_street(args, assistant))
        elif command == "remove-building":
            print(remove_building(args, assistant))
        elif command == "remove-apartment":
            print(remove_apartment(args, assistant))
        elif command == "add-birthday":
            print(add_birthday(args, assistant))
        elif command == "change-birthday":
            print(change_birthday(args, assistant))
        elif command == "add-note":
            print(add_note(notes))
        elif command == "all-notes":
            show_notes(notes)
        elif command == "all":
            show_contacts(assistant)
        else:
            print(Constants.INVALID_COMMAND_ERROR.value)


def save_data_address_book(assistant, filename="personal_assistant.pkl"):
    with open(filename, "wb") as fh:
        # noinspection PyTypeChecker
        pickle.dump(assistant, fh)


def save_data_notes(notes, filename="notes.pkl"):
    with open(filename, "wb") as fh:
        # noinspection PyTypeChecker
        pickle.dump(notes, fh)


def load_data_address_book(filename="personal_assistant.pkl"):
    try:
        with open(filename, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        return PersonalAssistant()


def load_data_notes(filename="notes.pkl"):
    try:
        with open(filename, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        return Notes()

if __name__ == "__main__":
    main()
