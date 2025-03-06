filename = input("Enter the file name: ")
file = open(filename, "r")

while True:
    pos = int(input("Enter position to read (negative to exit): "))
    if pos < 0:
        break
    file.seek(pos)
    char = file.read(1)  
    print("Character at position", pos, ":", char)

file.close()
