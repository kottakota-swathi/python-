class Example:
    static_var = int(input("Enter a static variable value: "))  

    @classmethod
    def change_static(cls, new_value):
        cls.static_var = new_value  

print("Before Change:", Example.static_var)

new_value = int(input("Enter new value for static variable: "))
Example.change_static(new_value)

print("After Change:", Example.static_var)
