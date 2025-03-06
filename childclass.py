class AbstractClass:
    def abstract_method(self):
        raise NotImplementedError("Subclasses must implement this method")

    def non_abstract_method(self):
        print("This is a non-abstract method")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in ConcreteClass")

    def create_instance_and_call(self):
        obj = ConcreteClass()  # Creating an instance of itself
        obj.abstract_method()  # Calling abstract method
        obj.non_abstract_method()  # Calling non-abstract method

child = ConcreteClass()
child.create_instance_and_call()
