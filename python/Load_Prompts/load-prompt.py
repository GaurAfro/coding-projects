
import json
import os

DATABASE_PATH = "load_prompt_database.json"

def load_prompt_database_json():
    # Check if the database file exists
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, 'r') as file:
            entries = json.load(file)
    else:
        # If the file doesn't exist, initialize an empty list
        entries = []

    return entries

def add_prompt(category, sub_category, title, text, time):
    # Load the existing entries from the database
    entries = load_prompt_database_json()

    # Construct a dictionary for the new prompt using the provided parameters
    prompt = {
        "category": category,
        "sub_category": sub_category,
        "title": title,
        "text": text,
        "time": time
    }

    # Append the new prompt to the entries list
    entries.append(prompt)

    # Save the updated entries list back to the JSON file
    with open(DATABASE_PATH, 'w') as file:
        json.dump(entries, file)

def main():
    # Define possible categories (you can update or add more as needed)
    quick = "quick"
    complete = "complete"
    template = "template"
    element = "element"

    # Call the add_prompt function with sample data to test it
    add_prompt(quick, "sub_category_example", "Sample Title", "Sample Text", "2023-07-19 12:16")

if __name__ == "__main__":
    main()
