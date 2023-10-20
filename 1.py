from bs4 import BeautifulSoup

# Read the HTML file
with open('grade.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <header> elements
header_elements = soup.find_all('footer')

# Replace each <header> element with a <script> element
for header_element in header_elements:
    script_tag = soup.new_tag('footer')
    script_tag.string = """<div id='foot'>
    <!-- Content will be loaded here using JavaScript -->
</div>

<script>
    // Function to fetch and replace content
    function replaceContent() {
        fetch('footer.html')
            .then(response => response.text())
            .then(data => {
                document.getElementById('foot').innerHTML = data;
            })
            .catch(error => console.error(error));
    }
    replaceContent();

</script># You can specify your script conheretent """  
    header_element.replace_with(script_tag)

# Write the modified HTML back to a file
with open('gra_de.html', 'w', encoding='utf-8') as output_file:
    output_file.write(str(soup))

print('Replacement completed.')
