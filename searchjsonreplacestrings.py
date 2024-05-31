import os
import json
import path

# Specify the root directory
root_dir = path.path

# Read search terms and replacements from files
with open('searchterms.txt', 'r') as f:
    search_terms = f.read().splitlines()

with open('replacements.txt', 'r') as f:
    replacements = f.read().splitlines()

# Function to replace terms in a dictionary
def replace_terms_in_dict(d):
    for term, replacement in zip(search_terms, replacements):
        d = d.replace(term, replacement)
    return d

# Walk through directories and subdirectories
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                data = f.read()
            new_data = replace_terms_in_dict(data)
            with open(file_path, 'w') as f:
                f.write(new_data)
            print(f"{file_path} has had its json replaced")