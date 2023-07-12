def save_to_history(role, message, filename="chat_history.txt"):
    # If the file exists, get the current max line number
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            last_message = [line for line in lines if ': ' in line][-1]
            current_message_num = int(last_message.split('.')[0]) + 1
    except (FileNotFoundError, IndexError, ValueError):
        # If any errors occur (like the file doesn't exist or is empty), start at 1
        current_message_num = 1

    with open(filename, "a") as file:
        file.write(f"{current_message_num}. {role}:\n{message}\n")


def main():
    # Start with the 'User' role
    role = 'User'

    while True:
        # Only display the quit option when the role is 'User'
        quit_option = " (or 'N' to finish)" if role == 'User' else ""
        print(f"Please paste the {role}'s message{quit_option}:")
        message = input()

        # Check if the user wants to finish
        if role == 'User' and message.strip().lower() == 'n':
            break

        # Save the message to the history file
        save_to_history(role, message)

        # Switch the role for the next interaction
        role = 'ChatGPT' if role == 'User' else 'User'


if __name__ == "__main__":
    main()
