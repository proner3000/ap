from bs4 import BeautifulSoup

# Read the HTML file
with open('2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <header> elements
header_elements = soup.find_all('header')

# Replace each <header> element with a <script> element
for header_element in header_elements:
    script_tag = soup.new_tag('script')
    script_tag.string = 'app'  # You can specify your script content here
    header_element.replace_with(script_tag)

# Write the modified HTML back to a file
with open('your_output_file.html', 'w', encoding='utf-8') as output_file:
    output_file.write(str(soup))

print('Replacement completed.')
