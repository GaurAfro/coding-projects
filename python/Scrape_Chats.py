import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage you want to scrape
url = "https://chat.openai.com/?model=gpt-4-code-interpreter"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Define the text string or pattern you're searching for
search_text = "I want to make a program with python"

# Find all tags that contain the search text
tags_with_text = soup.find_all(string=re.compile(search_text))

# Open a file to write the output
with open('output.txt', 'w') as f:
    # Iterate over the tags that contain the search text
    for tag in tags_with_text:
        # Write the parent tag and its contents to the file
        f.write(str(tag.parent))
        f.write("\n\n")  # Add some blank lines for readability
