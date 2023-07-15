# I want to copy the chat log from the chat that I have with any LLM and paste it into a text file,
# The text file should be saved in the folder of the LLM.
# There should be a different folder for each LLM.
# The text file should be named after the LLM.
# The text file should be named after the date of the chat.
# The text file should be named after the time of the chat.

# Imports
import pyperclip 
import tkinter as tk


# Functions

def copy_to_clipboard(text):
    pyperclip.copy(text)
    
def paste_from_clipboard():
    return pyperclip.paste()

    
# Classes 

class ChatConversation:
    
    def __init__(self, title):
        self.title = title
        self.messages = []
        
    def add_message(self, message):
        """Add message to chat history"""
        self.messages.append(message)


class ClaudeChat(ChatConversation):

        def __init__(self):
            super().__init__("Claude")

            
class GPTChat(ChatConversation):

        def __init__(self):
             super().__init__("GPT")
             

# Tkinter GUI code

root = tk.Tk()
root.title("AfroMemo") 


# Chat objects
my_chat_with_claude = ClaudeChat()
my_chat_with_gpt = GPTChat()