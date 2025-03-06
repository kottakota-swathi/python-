str1 = input("Enter the string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
str2 = input("Enter another string to compare: ")

if str1.startswith(prefix):
    print("String starts with the given prefix.")
else:
    print("String does not start with the given prefix.")

if str1.endswith(suffix):
    print("String ends with the given suffix.")
else:
    print("String does not end with the given suffix.")

if str1 == str2:
    print("Both strings are equal.")
elif str1 > str2:
    print("First string is greater.")
else:
    print("Second string is greater.")
