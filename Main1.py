class A:
    def __init__(self):
        self.__private_field = "Private Field in Class A"

    def __private_method(self):
        print("Private Method in Class A")

    def access_private(self):
        print("Accessing Private Field inside Class A:", self.__private_field)
        self.__private_method()

class B(A):
    def __init__(self):
        super().__init__()

    def try_access_private(self):
        # Trying to access private field (will cause an error)
        try:
            print("Trying to access:", self.__private_field)
        except AttributeError:
            print("Cannot access private field from subclass!")

        # Trying to call private method (will cause an error)
        try:
            self.__private_method()
        except AttributeError:
            print("Cannot call private method from subclass!")

class Main:
    @staticmethod
    def main():
        obj_A = A()
        print("\nAccessing Private Field and Method inside the same Class:")
        obj_A.access_private()  # Accessing private members within the class

        print("\nTrying to access private members from Subclass:")
        obj_B = B()
        obj_B.try_access_private()

Main.main()
