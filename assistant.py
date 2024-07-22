from errors_helper import input_error

# Description of what program can do
SUPPORTED_COMMANDS_INFO = """
Supported list of commands:
hello -> just says hi!
add 'name' 'phone' -> saves phone number by name
change 'name' 'phone' -> edits phone number by name
phone 'name' -> outputs saved phone number for this name
all -> output all saved contacts
close -> finish assistant
exit -> finish assistant
info -> information about supported commands

Make sure you follow the format of commands, and avoid spaces in phone numbers, as they are not supported."""

@input_error # use @input_error even for main() function to completely get rid of try/except here
def main():
    # greetings to user + list of supported commands
    print("Welcome to the assistant bot!")
    print(format_info())
    
    # waits for user's commands forever, untill terminal command is occurred
    contacts = {}
    while True:
        user_input = input("Enter a command: ")

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(find_number_by_name(args, contacts))
        elif command == "all":
            print(output_all_contacts(contacts))
        elif command == "info":
            print(format_info())
        else:
            print("Invalid command.")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def output_all_contacts(contacts):
    if len(contacts) > 0:
        return f"Here's all added contacts:\n{contacts}."
    else:
        return "No contacts added so far."

@input_error
def find_number_by_name(args, contacts):
    name = args[0]
    phone = contacts[name]

    return f"Phone number of {name}: {phone}."

    
@input_error
def change_contact(args, contacts):
    name, phone = args

    contacts[name] = phone
    return "Contact changed."


@input_error
def format_info():
    return SUPPORTED_COMMANDS_INFO

if __name__ == "__main__":
    # run program
    main()