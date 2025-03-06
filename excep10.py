try:
    class_name = input("Enter class name: ")
    class_obj = globals()[class_name]  # Tries to fetch the class dynamically
    obj = class_obj()  # Creates an instance if class exists
    print("Class instance created successfully!")

except KeyError:
    print(f"Error: Class '{class_name}' not found!")  
