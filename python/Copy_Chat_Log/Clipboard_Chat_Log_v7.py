# Import necessary modules
import pyperclip  # Allows access to the clipboard for copy-paste operations
import os         # Provides functions for interacting with the operating system
import msvcrt     # Provides functions for working with Microsoft Visual C Runtime, useful for keypress detection in this case
import json       # Provides JSON related operations

def log_chat_json_v7(filename_json, person1, person2):
    # Initialize variables for storing last entry's number and person
    last_number, last_person = 0, None
    chat_log = []

    # Check if a JSON file already exists
    if os.path.exists(filename_json):

        # Open the existing JSON file in read mode
        with open(filename_json, 'r') as file:

            # Load the JSON file into chat_log list
            chat_log = json.load(file)

            # If the chat_log is not empty
            if chat_log:

                # Get the last entry from the log
                last_entry = chat_log[-1]

                # Extract the last number and person from the last entry
                last_number = last_entry['number']
                last_person = last_entry['person']

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
        print("Press F1 to copy clipboard content to the log, or Esc to exit...")

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

                    # Add the clipboard content to the chat log as a dictionary
                    chat_log.append({'number': i, 'person': turn, 'message': clipboard_content})

                    # Open the JSON file in write mode
                    with open(filename_json, 'w') as file:

                        # Write the updated chat log to the JSON file
                        json.dump(chat_log, file, indent=4)

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

# Call the function with a JSON filename and two participants
log_chat_json_v7("chat_log_v7.json", "GaurAfro", "ChatGPT")
