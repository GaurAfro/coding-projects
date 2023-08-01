'''
---

**Pseudocode:**

1. **Initialization**:
    - Initialize `current_speaker` to `None`.
    - Initialize an empty list, `current_message`.
    - Initialize an empty list, `structured_data`.

2. **Find the start of the conversation**:
    - Iterate through `lines` to find the sequence "Code Interpreter", "Custom instructions details", and "User". Mark the index right after this sequence as `start_index`.

3. **Extract the conversation**:
    - For each `line` in `lines` starting from `start_index`:
        - If the `line` matches the exact pattern "User":
            - If `current_message` exists and `current_speaker` is not None, append a dictionary with `current_speaker` and the combined `current_message` to `structured_data`.
            - Reset `current_message` to an empty list.
            - Set `current_speaker` to "User".
        - Else if the `line` matches the exact pattern "ChatGPT":
            - If `current_message` exists and `current_speaker` is not None, append a dictionary with `current_speaker` and the combined `current_message` to `structured_data`.
            - Reset `current_message` to an empty list.
            - Set `current_speaker` to "ChatGPT".
        - Else, if `current_speaker` is set (not None):
            - Append the `line` (in its original form) to `current_message`.

4. **Finalize**:
    - If there's any remaining `current_message` after iterating through all lines, append it to `structured_data` as the final entry.

5. **Return**:
    - Return the `structured_data` list.

---

The result of the extraction process based on the latest changes is a structured list of dictionaries. Each dictionary has two keys: `speaker` (indicating either "User" or "ChatGPT") and `message` (containing the original, unchanged lines spoken by the speaker).
'''
import re
import json

def extract_and_structure_to_json_v3(lines):
    # Initialize variables
    current_speaker = None
    current_message = []
    structured_data = []

    # Determine the start of the conversation
    start_index = 0
    for i in range(len(lines)):
        if (i + 2 < len(lines) and
            lines[i] == "Code Interpreter" and
            lines[i + 1] == "Custom instructions details" and
            re.match(r'^User$', lines[i + 2])):
            start_index = i + 3
            break

    # Process the lines after the start of the conversation
    for line in lines[start_index:]:
        # Check if the line matches the 'User' pattern
        if re.match(r'^User$', line):
            # Save the current_message if it exists
            if current_message and current_speaker:
                structured_data.append({
                    'speaker': current_speaker,
                    'message': "".join(current_message)
                })
                current_message = []
            current_speaker = 'User'
        # Check if the line matches the 'ChatGPT' pattern
        elif re.match(r'^ChatGPT$', line):
            # Save the current_message if it exists
            if current_message and current_speaker:
                structured_data.append({
                    'speaker': current_speaker,
                    'message': "".join(current_message)
                })
                current_message = []
            current_speaker = 'ChatGPT'
        elif current_speaker:
            current_message.append(line)

    # Append any remaining messages
    if current_message and current_speaker:
        structured_data.append({
            'speaker': current_speaker,
            'message': "".join(current_message)
        })

    return structured_data

# Reading the file content
with open("/path_to_your_file.txt", "r") as file:
    content = file.readlines()

# Extract and structure the conversation
structured_data = extract_and_structure_to_json_v3(content)

# Convert the structured data to a JSON string
structured_json = json.dumps(structured_data, indent=4)

# Write the JSON string to a new file
with open("/path_to_output_file.json", "w") as file:
    file.write(structured_json)
'''
Replace "/path_to_your_file.txt" with the path to the file you want to process and "/path_to_output_file.json" with the path where you want the JSON output to be saved.
'''
