from Handler import add_record, show_contacts
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
            try:
                add_record(args, assistant)
            except ValueError as e:
                print(e)
        # elif command == "change":
            # print(assistant.change_contact(args, contact))
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