import os
import unittest

class TestChatHistory(unittest.TestCase):
    def setUp(self):
        self.filename = "test_chat_history.txt"
        # Ensure we're starting with a blank file
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        # Clean up the file after tests
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_to_history(self):
        # Write some messages
        save_to_history('User', 'Hello, ChatGPT!', self.filename)
        save_to_history('ChatGPT', 'Hello, User!', self.filename)

        # Read the file and check its content
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            self.assertEqual(lines[0], '1. User:\n')
            self.assertEqual(lines[1], 'Hello, ChatGPT!\n')
            self.assertEqual(lines[2], '2. ChatGPT:\n')
            self.assertEqual(lines[3], 'Hello, User!\n')

if __name__ == "__main__":
    unittest.main()
