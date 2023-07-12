# Import necessary modules
import pyperclip  # Allows access to the clipboard for copy-paste operations
import os         # Provides functions for interacting with the operating system
import re         # Provides regular expression matching operations
import msvcrt     # Provides functions for working with Microsoft Visual C Runtime, useful for keypress detection in this case

# Function to log chat between person1 and person2
def log_chat_v5(filename, person1, person2):

    # Initialize variables for storing last entry's number and person
    last_number, last_person = 0, None

    # Check if a log file already exists
    if os.path.exists(filename):

        # Open the existing log file in read mode
        with open(filename, 'r') as file:

            # Read all lines from the file
            lines = file.readlines()

            # Loop through the lines in reverse order (i.e., from last to first)
            for line in reversed(lines):

                # Try to find a match in the line for the pattern "number. person:"
                match = re.search(r'^(\d+)\. (.*?):', line)

                # If a match is found
                if match:
                    # Extract the last number and person from the match
                    last_number = int(match.group(1))
                    last_person = match.group(2)

                    # Break the loop as we've found the last logged entry
                    break

    # Determine whose turn it is based on who was the last person to speak
    if last_person == person1:
        turn = person2
    else:
        turn = person1

    # Start logging from the next number
    i = last_number + 1

    # Infinite loop to continuously log the chat
    while True:

        # Display instructions to the user
        print("Press F1 to copy clipboard content to the log file, or Esc to exit...")

        # Wait for a key press and store the pressed key
        key = msvcrt.getch()

        # If the key pressed is an arrow or function key
        if key in {b'\x00', b'\xe0'}:

            # If the key is F1
            if msvcrt.getch() == b';':

                # Get the current content of the clipboard
                clipboard_content = pyperclip.paste()

                # If there is any content in the clipboard
                if clipboard_content:

                    # Open the log file in append mode
                    with open(filename, 'a') as file:

                        # Write the content from the clipboard to the log file with the current number and person
                        file.write(f"{i}. {turn}: {clipboard_content}\n")

                    # Increment the number for the next entry
                    i += 1

                    # Switch the turn to the other person
                    if turn == person1:
                        turn = person2
                    else:
                        turn = person1

            # Continue with the next iteration of the loop
            continue

        # If the key is Esc, break the loop to exit the function
        elif key == b'\x1b':
            break

        # If any other key is pressed, show an error message and continue with the next iteration of the loop
        else:
            print("Invalid key. Please press F1 or Esc.")
            continue

        # If the clipboard is empty, show a message
        if not clipboard_content:
            print("Clipboard is empty. Please copy some text.")

# Call the function with a filename and two participants
log_chat_v5("chat_log_v5.txt", "GaurAfro", "ChatGPT")

'''
import pyperclip
import os
import re
import msvcrt

def log_chat_v5(filename, person1, person2):
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
        print("Press F1 to copy clipboard content to the log file, or Esc to exit...")
        key = msvcrt.getch()  # Wait for any key press
        if key in {b'\x00', b'\xe0'}:  # If it's an arrow or function key
            if msvcrt.getch() == b';':  # If the key is F1
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
            continue
        elif key == b'\x1b':  # If the key is Esc
            break
        else:
            print("Invalid key. Please press F1 or Esc.")
            continue
        if not clipboard_content:
            print("Clipboard is empty. Please copy some text.")

# Example usage:
log_chat_v5("chat_log_v5.txt", "GaurAfro", "ChatGPT")
'''