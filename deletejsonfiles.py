import os
import path

def delete_json_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                os.remove(os.path.join(root, file))
                print(f'Deleted: {os.path.join(root, file)}')

delete_json_files(path.path)
