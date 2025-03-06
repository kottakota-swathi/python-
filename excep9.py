filename = input("Enter file name: ")

file = open(filename, "r")  # This will raise FileNotFoundError if the file does not exist

content = file.read()
print(content)

file.close()
