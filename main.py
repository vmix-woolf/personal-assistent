from Handler import
from PersonalAssistant import PersonalAssistant
import pickle

def main():
    assistant = load_data()
    print(f"Welcome to personal assistant")

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


def save_data(book, filename="personal_assistant.pkl"):
    with open(filename, "wb") as fh:
        pickle.dump(book, fh)


def load_data(filename="personal_assistant.pkl"):
    try:
        with open(filename, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        return PersonalAssistant()


if __name__ == "__main__":
    main()