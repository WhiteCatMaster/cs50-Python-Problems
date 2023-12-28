'''
.gif -- image/gif
.jpg -- image/jpeg
.jpeg -- image/jpeg
.png -- image/png
.pdf -- application/pdf
.txt -- text/plain
.zip -- application/zip
'''
file = input("File name: ")
if ".gif" in file:
    print("image/jpeg")
elif ".jpg" or ".jpge" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")