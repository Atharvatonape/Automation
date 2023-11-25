import os
import shutil

def organize_directory(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    # Get list of files in the directory
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:
        # Get file extension
        file_extension = file.split('.')[-1]

        # Create a folder for the extension if it doesn't exist
        folder_path = os.path.join(path, file_extension)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # Move file to the corresponding folder
        shutil.move(os.path.join(path, file), folder_path)

    print("Files have been organized.")

# Use the function
directory_path = "C:\\Users\\Lenovo\\Downloads"  # Replace with your directory path
organize_directory(directory_path)
