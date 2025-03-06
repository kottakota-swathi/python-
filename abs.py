class AbstractClass:
    def abstract_method(self):
        raise NotImplementedError("Subclasses must implement this method")

    def non_abstract_method(self):
        print("This is a non-abstract method")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in ConcreteClass")

obj = ConcreteClass()
obj.abstract_method()
obj.non_abstract_method()
