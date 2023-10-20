# Read names from the file
with open('a.txt', 'r') as file:
    names = file.read().splitlines()

# Use a set to store unique names
unique_names = set(names)

# Write unique names back to the file
with open('qw.txt', 'w') as file:
    file.write("[")     
    for name in unique_names:
     if(name!="notes.html" and name!="index.html" and name!="support.html" and name!="about.html" and name!="contact.html"):
       file.write('"'+name + '",')
    file.write("]")