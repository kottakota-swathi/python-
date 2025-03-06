filename = input("Enter the file name: ")

file = open(filename, "r")
content = ""

while True:
    line = file.readline()
    if not line:
        break
    content += line

file.close()

print("File Content:\n", content)
