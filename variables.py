# Global variable
message = "I am a global variable"

def my_function():
    # Local variable (same name as global)
    message = "I am a local variable"
    print("Inside function:", message)  # Prints local variable

# Calling the function
my_function()

# Printing the global variable
print("Outside function:", message)  # Prints global variable
