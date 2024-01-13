import os

# Specify the directory path
directory_path = 'output_tiles'

# List all files in the directory
files = os.listdir(directory_path)

# Iterate through the files and rename them
for index, file in enumerate(files):
    # Specify the new name (you can modify this based on your requirements)
    new_name = f"tile_{index}.png"
    
    # Construct the full paths for the old and new names
    old_path = os.path.join(directory_path, file)
    new_path = os.path.join(directory_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)

print("Files renamed successfully.")
