filename = input("Enter the file name: ")
file = open(filename, "r")

index = int(input("Enter the index to start reading from: "))

file.seek(index)

while True:
    char = file.read(1)  
    if not char:  
        break
    print(char, end="")  

file.close()
