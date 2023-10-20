import os

# Define the folder name and file name
folder_name = "optmath"

# Check if the folder already exists
if not os.path.exists(folder_name):
    # If it doesn't exist, create the folder
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' has been created.")

# Create and write to the file inside the folder
for i in range (1,10):
    file_name = "modelset-"+ str(i) + ".html"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w') as file:
        file.write("")

print(f"File '{file_name}' has been created inside '{folder_name}'.")
