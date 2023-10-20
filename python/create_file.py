# Specify the source file containing the data
source_filename = "grade.html"

# Read data from the source file
with open(source_filename, "r") as source_file:
    data_to_write = source_file.read()

# Specify the file names in an array
file_names = ["notes.html","about.html","support.html","contact.html","ss.html","index.html","bachelor.html","+2.html"]

# Create and write data to the destination files
for filename in file_names:
    with open(filename, "w") as destination_file:
        destination_file.write(data_to_write)
    print(f"Created file: {filename}")
