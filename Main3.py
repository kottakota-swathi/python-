class Parent:
    def __init__(self):
        self.public_field = "This is a public field"

    def public_method(self):
        print("This is a public method")

class Child(Parent):
    def access_public(self):
        print("Accessing Public Field in Child Class:", self.public_field)
        self.public_method()

class OtherClass:
    def access_public(self):
        parent = Parent()
        print("Accessing Public Field in Another Class:", parent.public_field)
        parent.public_method()

parent_obj = Parent()
print("Accessing Public Field in Parent Class:", parent_obj.public_field)
parent_obj.public_method()

child_obj = Child()
child_obj.access_public()

other_class_obj = OtherClass()
other_class_obj.access_public()
