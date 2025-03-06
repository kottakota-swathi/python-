def fullmatch(pattern, string):
    if pattern == string:
        return True
    return False

string = input("Enter a string: ")
pattern = input("Enter a pattern: ")

if fullmatch(pattern, string):
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")
