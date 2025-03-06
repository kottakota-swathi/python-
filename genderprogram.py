def print_gender(g):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    print(switch.get(g.upper(), "Invalid input"))

gender = input("Enter M or F: ")
print_gender(gender)
