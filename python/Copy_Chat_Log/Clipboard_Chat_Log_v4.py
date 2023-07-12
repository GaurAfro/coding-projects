
import msvcrt
import os
import re

import pyperclip


def log_chat_v4(filename, person1, person2):
    # Check if the log file exists and get the last entry's number and person
    last_number, last_person = 0, None
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):  # Look at the log from the end
                match = re.search(r'^(\d+)\. (.*?):', line)  # Extract the number and person
                if match:  # If a valid log entry is found
                    last_number = int(match.group(1))  # Get the last number used
                    last_person = match.group(2)  # Get the last person who spoke
                    break

    # Determine whose turn it is
    if last_person == person1:
        turn = person2
    else:
        turn = person1

    # Start the conversation log from where it left off
    i = last_number + 1
    while True:
        print("Press Enter to copy clipboard content to the log file...")
        key = msvcrt.getch()  # Wait for any key press
        if key == b'\r':  # If the key is Enter
            clipboard_content = pyperclip.paste()
            if clipboard_content:
                with open(filename, 'a') as file:
                    file.write(f"{i}. {turn}: {clipboard_content}\n")
                i += 1
                # Switch turn
                if turn == person1:
                    turn = person2
                else:
                    turn = person1
        else:
            print("Please press Enter.")
            continue
        if not clipboard_content:
            print("Clipboard is empty. Please copy some text.")

# Example usage:
log_chat_v4("chat_log_v4.txt", "GaurAfro", "ChatGPT")
