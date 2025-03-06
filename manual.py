filename = input("Enter the file name: ")

try:
    file = open(filename, "r")
    file.close()
    can_read = True
except:
    can_read = False

try:
    file = open(filename, "a")
    file.close()
    can_write = True
except:
    can_write = False

print("Read Access:", "Yes" if can_read else "No")
print("Write Access:", "Yes" if can_write else "No")
