class ClassOne:
    def __init__(self, name):
        self.name = name

    def display_one(self):
        print("ClassOne Method: Name is", self.name)

class ClassTwo:
    def __init__(self, age):
        self.age = age

    def display_two(self):
        print("ClassTwo Method: Age is", self.age)

obj1 = ClassOne("AIthi")
obj1.display_one()

obj2 = ClassTwo(25)
obj2.display_two()
