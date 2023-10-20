import os
import fileinput

# Define the directory where you want to search for files
directory = 'C:/Users/kairn/Music/khusbunotes/'

# Function to search and replace in a single file
def replace_in_file(file_path):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(line.replace('KhusbuKhadka.com', 'khushankhadka.com'), end='')

# Recursively search for files in the directory
for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        if file_path.endswith('.html'):  # Adjust the file extension as needed
            replace_in_file(file_path)
            print(file_path)
