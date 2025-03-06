def relational_operators():
    # Taking input from the user
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # Performing relational operations
    print(f"{a} < {b}  --> {a < b}")   
    print(f"{a} <= {b} --> {a <= b}")  
    print(f"{a} > {b}  --> {a > b}")   
    print(f"{a} >= {b} --> {a >= b}")  

# Calling the function
relational_operators()
