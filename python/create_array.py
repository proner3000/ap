
with open("array.txt", "r") as htmlcode1:
    html_code = htmlcode1.read()

with open('ready_made_array.txt', 'w') as file:
    file.write(html_code + ',')