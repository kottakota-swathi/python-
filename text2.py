filename = input("Enter the file name: ")

file = open(filename, "w")

while True:
    text = input("Enter text (type 'exit' to stop): ")
    if text == "exit":
        break
    file.write(text + "\n")

file.close()

print("Text written successfully to", filename)
