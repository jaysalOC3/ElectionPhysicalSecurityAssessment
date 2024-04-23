import os

# List of folder paths
folder_paths = [
    "./Docs/Models/",
    # Add more folder paths as needed
]

# Function to print files and their contents
def print_files_in_folder(folder_path):
    # Get a list of files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file in the folder
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the current item is a file (not a directory)
        if os.path.isfile(file_path):
            # Open the file and read its contents
            with open(file_path, "r") as file:
                file_contents = file.read()
                
                # Print the file name and its contents
                print(f"File: {file_name}")
                print(file_contents)
                print()  # Print an empty line for separation

# Iterate over each folder path in the list
for folder_path in folder_paths:
    print(f"Folder: {folder_path}")
    print_files_in_folder(folder_path)
    print("=" * 40)  # Print a separator line between folders