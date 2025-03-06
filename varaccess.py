class Example:
    static_var = int(input("Enter a static variable value: "))  

    def access_static(self):
        return self.static_var  

obj = Example()
print("Accessed via Instance:", obj.access_static())
