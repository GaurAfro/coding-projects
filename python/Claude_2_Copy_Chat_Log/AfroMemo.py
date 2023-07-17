# Imports
import pyperclip
import tkinter as tk
from collections import deque

# Functions


def main():
    my_chat = ChatConversation("My Chat")
    my_chat.add_message("Hello")

    print(my_chat.messages)


def copy_to_clipboard(text):
    """Copy text to clipboard"""
    pyperclip.copy(text)


def paste_from_clipboard():
    """Paste text from clipboard"""
    return pyperclip.paste()


# Classes


class ChatConversation:
    """Chat conversation class"""


    def __init__(self, title):
        self.title = title
        self.messages = []

    def add_message(self, message):
        """Add message to chat"""
        self.messages.append(message)


class ClaudeChat(ChatConversation):

    def __init__(self):
        super().__init__("Claude")


class GPTChat(ChatConversation):

    def __init__(self):
        super().__init__("GPT")


# Data structures
chats = {
    "Chat with Claude": "",
    "Chat with GPT": ""
}

clipboard_history = deque(maxlen=100)
pinned_items = []
frequent_items = {
    "example": 0
}


def add_to_clipboard(text):

    if text in clipboard_history:
        clipboard_history.remove(text)

    clipboard_history.append(text)


def pin_item(text):
    pinned_items.append(text)


# GUI
root = tk.Tk()
root.title("AfroMemo")

# Main
if __name__ == "__main__":
    main()
