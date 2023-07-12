
import re

def save_to_history(role, message, filename="chat_history.txt"):
    # If the file exists, get the current max line number
    current_message_num = 1
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                if re.match(r"\d+\.\s(ChatGPT|User):", line):
                    current_message_num = int(line.split('.')[0]) + 1
                    break
    except (FileNotFoundError, IndexError, ValueError):
        # If any errors occur (like the file doesn't exist or is empty), start at 1
        pass

    with open(filename, "a") as file:
        file.write(f"{current_message_num}. {role}:
{message}\n")

def main():
    # Start with the 'User' role
    role = 'User'

    while True:
        if role == 'User':
            print("Do you have more chats to copy? (Y/N)")
            more_chats = input()
            if more_chats.lower().startswith('n'):
                break

        print(f"Please paste the {role}'s message:")
        message = input()

        # Save the message to the history file
        save_to_history(role, message)

        # Switch the role for the next interaction
        role = 'ChatGPT' if role == 'User' else 'User'

if __name__ == "__main__":
    main()
