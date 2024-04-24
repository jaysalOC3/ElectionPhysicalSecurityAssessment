import os

# List of folder paths
folder_paths = [
    "./Docs/apps/Assessment/Model",
    "./Docs/apps/Assessment/View",
    "./Docs/apps/Assessment/Form",
    "./Docs/apps/PollingSite/Model",
    "./Docs/apps/PollingSite/View",
    "./Docs/apps/PollingSite/Form",
    "./Docs/apps/User/Model",
    "./Docs/apps/User/View",
    "./Docs/apps/User/Form",
    # Add more folder paths as needed
]

# List of individual file paths
individual_files = [
    "README.md",
    # Add more individual file paths as needed
]

# Function to print files and their contents
def print_file_contents(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        # Open the file and read its contents
        with open(file_path, "r") as file:
            file_contents = file.read()
        
        # Print the file name and its contents
        print(f"Python django File: {file_path}")
        print(file_contents)
        print()  # Print an empty line for separation
    else:
        print(f"File not found: {file_path}")
        print()  # Print an empty line for separation

# Function to print files and their contents in a folder
def print_files_in_folder(folder_path):
    # Get a list of files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file in the folder
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the current item is a file (not a directory)
        if os.path.isfile(file_path):
            print_file_contents(file_path)

# Print individual files
print("Individual Files:")
for file_path in individual_files:
    print_file_contents(file_path)
print("=" * 40)  # Print a separator line

# Print files in folders
for folder_path in folder_paths:
    print(f"Folder: {folder_path}")
    print_files_in_folder(folder_path)
    print("=" * 40)  # Print a separator line between folders