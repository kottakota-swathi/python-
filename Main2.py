class Parent:
    def __init__(self):
        self._protected_field = "This is a protected field"

    def _protected_method(self):
        print("This is a protected method")

class Child(Parent):
    def access_protected(self):
        print("Accessing Protected Field in Child Class:", self._protected_field)
        self._protected_method()

class OtherClass:
    def access_protected(self):
        parent = Parent()
        print("Accessing Protected Field in Another Class:", parent._protected_field)
        parent._protected_method()

parent_obj = Parent()
print("Accessing Protected Field in Parent Class:", parent_obj._protected_field)
parent_obj._protected_method()

child_obj = Child()
child_obj.access_protected()

other_class_obj = OtherClass()
other_class_obj.access_protected()
