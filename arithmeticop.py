def arithmetic_operations(a, b):
    # Performing arithmetic operations
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Cannot divide by zero"

    # Printing results
    print(f"Addition: {a} + {b} = {addition}")
    print(f"Subtraction: {a} - {b} = {subtraction}")
    print(f"Multiplication: {a} * {b} = {multiplication}")
    print(f"Division: {a} / {b} = {division}")

# Calling the function with example values
arithmetic_operations(10, 5)
