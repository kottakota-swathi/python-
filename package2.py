# Simulating a package structure
class PackageOne:
    class FirstClass:
        def __init__(self, data1):
            self.data1 = data1

        def show_first(self):
            print("FirstClass Data:", self.data1)

class PackageTwo:
    class SecondClass:
        def __init__(self, data2):
            self.data2 = data2

        def show_second(self):
            print("SecondClass Data:", self.data2)

# Importing from the simulated packages
FirstClass = PackageOne.FirstClass
SecondClass = PackageTwo.SecondClass

# Creating objects and calling methods
first_obj = FirstClass("AIthi")
first_obj.show_first()

second_obj = SecondClass(2025)
second_obj.show_second()
