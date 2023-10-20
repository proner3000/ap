import re

source_filename= "s.html"

with open(source_filename, "r") as a:
    html_code = a.read()

matches = re.findall(r'(\w+)\.html', html_code)

# Print the matches
with open("a.txt", "w") as output_file:
 for match in matches:
   output_file.write(match+".html\n")

# with open("append.txt", "a") as destination_file:
#  destination_file.write(html_code)
 