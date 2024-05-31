import os
import path

def search_and_list_files(folder_path, target_folder_name, output_file):
    """
    Recursively searches for a specific folder and lists files within it.
    :param folder_path: Starting directory path
    :param target_folder_name: Name of the folder to search for
    :param output_file: Path to the output text file
    """
    with open(output_file, 'w') as txt_file:
        for root, dirs, files in os.walk(folder_path):
            if target_folder_name in dirs:
                target_folder_path = os.path.join(root, target_folder_name)
                for dirpath, dirnames, filenames in os.walk(target_folder_path):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        # Exclude files within the "mm" folder
                        if not file_path.startswith(os.path.join(target_folder_path, "mm")):
                            # Include the "data" folder in the path
                            relative_path = os.path.relpath(file_path, folder_path)
                            # Trim the line to start from the "data" directory
                            trimmed_path = os.path.join("data", relative_path)
                            txt_file.write(trimmed_path + '\n')

# Example usage:
data_directory = path.path
target_folder = 'structures'
output_txt_file = 'file_list.txt'

search_and_list_files(data_directory, target_folder, output_txt_file)
print(f"File paths listed in '{output_txt_file}'.")
