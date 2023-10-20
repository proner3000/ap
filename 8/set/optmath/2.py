import pyperclip

# Text you want to copy to the clipboard


# Copy the text to the clipboard
a=""
# Optionally, you can check if the copy was successful
for i in range (1,10):
    b = "modelset-"+ str(i) 
    a+='<a href="set/optmath/'+b+'.html"><li>'+b+'</li></a>\n'
pyperclip.copy(a)

if pyperclip.paste() == a:
    print("Text has been copied to the clipboard.")
else:
    print("Copy to clipboard failed.")