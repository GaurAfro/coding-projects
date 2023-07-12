# Import the necessary modules
import pyperclip
import os

# Define a function to log the chat
def log_chat(filename, GaurAfro, ChatGPT):
    # Initialize a counter
    i = 1

    # Start an infinite loop
    while True:
        # Wait for user input to proceed. This is where you press Enter to copy the clipboard content to the log
        input("Press Enter to copy clipboard content to the log file...")

        # Retrieve the current content of the clipboard
        clipboard_content = pyperclip.paste()

        # Check if the clipboard content is not empty
        if clipboard_content:
            # Open the log file in append mode
            with open(filename, 'a') as file:
                # If the counter is odd, it's GaurAfro's turn to speak
                if i % 2 != 0:
                    # Write GaurAfro's message to the file
                    file.write(f"{i}. {GaurAfro}: {clipboard_content}\n")
                # If the counter is even, it's ChatGPT's turn to speak
                else:
                    # Write ChatGPT's message to the file
                    file.write(f"{i}. {ChatGPT}: {clipboard_content}\n")

            # Increment the counter
            i += 1

        # If the clipboard is empty, print a message to let the user know
        else:
            print("Clipboard is empty. Please copy some text.")

# Call the function with the desired filename and person names
log_chat("chat_log.txt", "GaurAfro", "ChatGPT")
