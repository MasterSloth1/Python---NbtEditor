import os
import nbtlib
import json
import gzip
import tempfile
import path

# Function to convert a Python data type to an NBT tag
def convert_python_to_nbt(data):
    if isinstance(data, dict):
        return nbtlib.tag.Compound({name: convert_python_to_nbt(subdata) for name, subdata in data.items()})
    elif isinstance(data, list):
        return nbtlib.tag.List([convert_python_to_nbt(item) for item in data])
    elif isinstance(data, int):
        # Check if the integer is within the range of a 32-bit integer
        if -2147483648 <= data <= 2147483647:
            return nbtlib.tag.Int(data)
        else:
            return nbtlib.tag.Long(data)
    elif isinstance(data, str):
        return nbtlib.tag.String(data)
    elif isinstance(data, float):
        if data > 3.4028235e+38 or data < -3.4028235e+38:
            return nbtlib.tag.Double(data)
        else:
            return nbtlib.tag.Float(data)
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")

# Specify the root directory (change this to your desired directory)
root_dir = path.path

# Walk through the root directory
for dir_path, dir_names, file_names in os.walk(root_dir):
    # Process each file
    for file_name in file_names:
        # Check if the file is a .json file
        if file_name.endswith(".json"):
            # Construct the full file path
            json_file_path = os.path.join(dir_path, file_name)

            # Load the JSON data from the file
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)

            # Convert the JSON data to an NBT object
            nbt_data = convert_python_to_nbt(json_data)

            # Create a temporary file to save the NBT data
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file_path = temp_file.name
                nbtlib.File({'': nbt_data}).save(temp_file_path)

            # Construct the .nbt file path
            nbt_file_path = os.path.splitext(json_file_path)[0] + ".nbt"

            # Save the NBT data to a gzipped file
            with gzip.open(nbt_file_path, 'wb') as gzipped_file:
                with open(temp_file_path, 'rb') as temp_nbt_file:
                    gzipped_file.write(temp_nbt_file.read())

            # Clean up the temporary file
            os.remove(temp_file_path)

    # Print a success message for the directory
    print(f"All .json files in {dir_path} have been converted to .nbt files and gzipped.")

print("Conversion completed successfully.")
