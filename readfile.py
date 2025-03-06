filename = input("Enter the file name: ")

file = open(filename, "r")

while True:
    char = file.read(1)  
    if not char:  
        break
    print(char, end="")  

file.close()
