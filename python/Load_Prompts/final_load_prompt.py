
import json
import os
import pyperclip

# Define the file path for the database
DATABASE_PATH = "/home/gaurafro/coding-projects/python/Load_Prompts/load_prompt_database.json"

def format_entry(entry):
    formatted = (
        f"\nTime: {entry['time']}\n"
        f"Category: {entry['category'].capitalize()}\n"
        f"Subcategory: {entry['subcategory']}\n"
        f"Title: {entry['title']}\n"
        f"Text: {entry['text']}\n"
        "--------------------------"
    )
    return formatted

def load_prompt_database_json():
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, 'r') as file:
            entries = json.load(file)
    else:
        entries = []
    return entries

def view_all_entries():
    entries = load_prompt_database_json()
    formatted_entries_list = []
    
    for entry in entries:
        formatted_entry = (
            f"Time: {entry['time']}\n"
            f"Category: {entry['category'].capitalize()}\n"
            f"Subcategory: {entry['subcategory']}\n"
            f"Title: {entry['title']}\n"
            f"Text: {entry['text']}\n"
            "--------------------------"  # Separator for clarity between entries
        )
        formatted_entries_list.append(formatted_entry)

    formatted_entries = "\n".join(formatted_entries_list)
    pyperclip.copy(formatted_entries)
    print(formatted_entries)

def get_unique_categories():
    entries = load_prompt_database_json()
    categories = set(entry['category'] for entry in entries)
    return categories

def get_unique_subcategories():
    entries = load_prompt_database_json()
    subcategories = set(entry['subcategory'] for entry in entries)
    return subcategories

def get_unique_titles():
    entries = load_prompt_database_json()
    titles = set(entry['title'] for entry in entries)
    return titles   

def retrieve_by_category(desired_category):
    entries = load_prompt_database_json()
    filtered_entries = [entry for entry in entries if entry['category'] == desired_category]
    
    if not filtered_entries:
        print(f"No entries found for category: {desired_category}")
        return
    
    formatted_entries = [format_entry(entry) for entry in filtered_entries]
    result = "\n".join(formatted_entries)
    pyperclip.copy(result)
    print(result)
def retrieve_by_subcategory(desired_subcategory):
    entries = load_prompt_database_json()
    filtered_entries = [entry for entry in entries if entry['subcategory'] == desired_subcategory]
    
    if not filtered_entries:
        print(f"No entries found for subcategory: {desired_subcategory}")
        return
    
    formatted_entries = [format_entry(entry) for entry in filtered_entries]
    result = "\n".join(formatted_entries)
    pyperclip.copy(result)
    print(result)
def retrieve_by_title(desired_title):
    entries = load_prompt_database_json()
    matching_entry = next((entry for entry in entries if entry['title'] == desired_title), None)
    
    if not matching_entry:
        print(f"No entry found with title: {desired_title}")
        return
    
    result = format_entry(matching_entry)
    pyperclip.copy(result)
    print(result)
def main():
    while True:
        print("\nOptions:")
        print("1: View All Entries")
        print("2: Retrieve by Category")
        print("3: Retrieve by Subcategory")
        print("4: Retrieve by Title")
        print("5: Exit")
        
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            view_all_entries()
        
        elif choice == "2":
            unique_categories = get_unique_categories()
            print("Available Categories:")
            for category in unique_categories:
                print(f"- {category}")
            category = input("Enter your desired category from the list above: ")
            retrieve_by_category(category)
        
        elif choice == "3":
            unique_subcategories = get_unique_subcategories()
            print("Available Subcategories:")
            for subcategory in unique_subcategories:
                print(f"- {subcategory}")
            subcategory = input("Enter your desired subcategory from the list above: ")
            retrieve_by_subcategory(subcategory)

        elif choice == "4":
            unique_titles = get_unique_titles()
            print("Available Titles:")
            for title in unique_titles:
                print(f"- {title}")
            title = input("Enter your desired title from the list above: ")
            retrieve_by_title(title)
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
