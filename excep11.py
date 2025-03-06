try:
    filename = input("Enter file name: ")
    file = open(filename, "r")  # Raises an error if the file does not exist or cannot be opened
    content = file.read()
    print(content)
    file.close()

except OSError:
    print("Error: An I/O error occurred while accessing the file.")
