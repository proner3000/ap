# Define the file path
file_path = ["science.html","nepali.html","health.html","optmath.html","Mathematics.html","grammar.html","computer.html","english.html","socialstudies.html","account.html"]  # Replace with the path to your HTML file

for file_path in file_path:
    # Read the file and perform replacements
    with open(file_path, 'r') as file:
        content = file.read()

    # Define the HTML code block to be replaced
    original_html = """<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../../dark.css" rel="stylesheet">
    <!-- ALL SCRIPT -->
    <script src="https://kit.fontawesome.com/a142baf863.js" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="container-fluid ap" style="padding: 0 0 0 0">
            <nav class="pp">
                <div id="main" class="d">
                <span id="z" style="font-size:30px; cursor:pointer" onclick="openNav()">&#9776;</span>
                </div>
            <a class="navbar-brand b" href="../../index.html"> <img src="../../../images/1.png" class="bgg" style="height: 157px; "  > <img src="../../../images/2.jpg" class="c" style="width: 202px; " ></a>
            </nav>
            </div>   
    <div id="mySidenav" class="sidenav">
    <a href="javascript:void(0)" onclick="closeNav()"><i class='fas fa-angle-left'style='font-size:24px color:white;' ></i> Close</button>
        
            <a  href="../../index.html">Home</a>
            <a  href="../../about.html">About</a>
            <a  href="../../notes.html">Notes</a>
            <a  href="../../support.html">Support us</a>
            <a  href="../../contact.html">Contact us</a>
        </ul>
    </div>"""
    stripped_name = file_path.rsplit('.html', 1)[0]
    # Define the replacement HTML code
    replacement_html = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="/dark.css" rel="stylesheet">
        <title>"""+stripped_name+"""</title>
        <meta name="description" content="Welcome to KhusbuKhadka.com.np - Your Note-Taking Companion. Discover the power of organized knowledge with our easy-to-use note-taking tools. Capture and access your notes effortlessly, whether you're a student, a professional, or a lifelong learner. Join our community and elevate your learning experience today." >
        <link rel="canonical" href="https://www.khusbukhadka.com.np/9/set/"""+file_path+""">
        <meta name="author" content="khusbu khadka">
        <meta name="keywords" content="khusbu,khadka,khusbunotes,class,8,9,10 ,notes,nepal,nepali,math,science,setbook">
        <meta http-equiv="refresh" content="600;url=https://www.khusbukhadka.com.np/9/set/"""+file_path+""">
        <meta name="robots" content="index, nofollow">
        <link rel="canonical" href="https://www.khusbukhadka.com.np/9/set/"""+file_path+""">
        <meta property="og:title" content="Invitation to khusbukhadka.com.np">
        <meta property="og:description" content="KhusbuKhadka.com.np - Your Note-Taking Companion. Discover the power of organized knowledge with our easy-to-use note-taking tools(set solution). Capture and access your notes effortlessly, whether you're a student, a professional, or a lifelong learner. Join our community and elevate your learning experience today.Notes from 8-12">
        <meta property="og:image" content="/images/2.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Invitation to khusbukhadka.com.np">
    <meta name="twitter:description" content="KhusbuKhadka.com.np - Your Note-Taking Companion. Discover the power of organized knowledge with our easy-to-use note-taking tools. Capture and access your notes effortlessly, whether you're a student, a professional, or a lifelong learner. Join our community and elevate your learning experience today.Notes from 8-12">
    <meta name="twitter:image" content="/images/2.png">
    
    <!-- ALL SCRIPT -->
    <script src="/toggle.js" defer ></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://kit.fontawesome.com/a142baf863.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
    <div id="header">
    </div>"""

    # Perform the replacement
    content = content.replace(original_html, replacement_html)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print("File updated successfully.")
