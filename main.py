from Handler import (
    add_contact,
    change_contact,
    add_email,
    change_email,
    add_address,
    change_address,
    add_birthday,
    change_birthday,
    show_contacts
)
from PersonalAssistant import PersonalAssistant
from collections import UserDict

def main():
    assistant = PersonalAssistant()
    print(f"Welcome to personal assistant")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, assistant)
        elif command == "change":
            change_contact(args, assistant)
        elif command == "add-email":
            add_email(args, assistant)
        elif command == "change-email":
            change_email(args, assistant)
        elif command == "add-address":
            add_address(args, assistant)
        elif command == "change-address":
            change_address(args, assistant)
        elif command == "add-birthday":
            add_birthday(args, assistant)
        elif command == "change-birthday":
            change_birthday(args, assistant)
        elif command == "all":
            show_contacts(assistant)
        else:
            print("Invalid command.")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


if __name__ == "__main__":
    main()