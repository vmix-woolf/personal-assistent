from PersonalAssistant import PersonalAssistant
from Record import Record
import re


def add_record(args, assistant: PersonalAssistant):
    name, email, phone_number, *_ = args
    # if first_param is valid name then
    if name_verification(name):
        # if second_param is not valid surname then
        if name_verification(second_param):
        # if the number is valid phone number
            if phone_number_verification(number):
                name = first_param + ' ' + second_param
                record = Record(name)
                record.add_phone(number)
                assistant.add_record(record)
            else:
                raise ValueError('Invalid phone format')
        else:
            if phone_number_verification(number):
                name = first_param
                record = Record(name)
                record.add_phone(number)
                assistant.add_record(record)
            else:
                raise ValueError('Invalid phone format')
    # if first_param is not valid name then value error exception
    else:
        raise ValueError('Please input correct contact name')


def show_contacts(assistant: PersonalAssistant):
    if len(assistant) == 0:
        print('There are no contacts')
    else:
        for _, contact in assistant.items():
            print(contact)

def phone_number_verification(number):
    if number.isdigit() and len(number) == 3:
        return True
    else:
        return False

def name_verification(name):
    return True if bool(re.match(r'[A-Za-z]{2,25}', name)) else False

def email_verification(email):
    return True if bool(re.match(r'^[a-zA-Z0-9. _%+-]+@[a-zA-Z0-9. -]+\\. [a-zA-Z]{2,}$', email)) else False