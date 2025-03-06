class Example:
    static_var = int(input("Enter a static variable value: "))  

    def change_static(self, new_value):
        Example.static_var = new_value  

obj = Example()
print("Before Change:", obj.static_var)

new_value = int(input("Enter new value for static variable: "))
obj.change_static(new_value)

print("After Change:", obj.static_var)
print("Accessed via Class:", Example.static_var)
