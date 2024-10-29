import pickle
import constants
from PersonalAssistant import PersonalAssistant
from Handler import (
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
    showcase_contact
)


def main():
    assistant = load_data()
    print(constants.WELCOME_MESSAGE)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            save_data(assistant)
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
        elif command == "all":
            show_contacts(assistant)
        else:
            print(constants.INVALID_COMMAND_ERROR)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def save_data(book, filename="personal_assistant.pkl"):
    with open(filename, "wb") as fh:
        # noinspection PyTypeChecker
        pickle.dump(book, fh)


def load_data(filename="personal_assistant.pkl"):
    try:
        with open(filename, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        return PersonalAssistant()


if __name__ == "__main__":
    main()