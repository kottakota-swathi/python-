class Example:
    static_var = int(input("Enter a static variable value: "))  

    @classmethod
    def access_static(cls):
        return cls.static_var  

print("Static Variable:", Example.static_var)
print("Accessed via Method:", Example.access_static())
