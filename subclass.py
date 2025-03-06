class AbstractClass:
    def abstract_method(self):
        raise NotImplementedError("Subclasses must implement this method")

    def non_abstract_method(self):
        print("This is a non-abstract method")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in ConcreteClass")

    def access_abstract_class_methods(self):
        obj = AbstractClass()  # Creating an object of AbstractClass
        obj.non_abstract_method()  # Accessing non-abstract method

child = ConcreteClass()
child.access_abstract_class_methods()
