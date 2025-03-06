class MyClass:
    def __init__(self):  # Public Constructor
        print("Public Constructor Called")

    def _protected_init(self):  # Protected Constructor (Naming Convention)
        print("Protected Constructor Called")

    def __private_init(self):  # Private Constructor (Name Mangling)
        print("Private Constructor Called")

    def call_private(self):  
        self.__private_init()  

class ChildClass(MyClass):
    def __init__(self):
        super().__init__()  
        self._protected_init()  

obj1 = MyClass()  
obj1.call_private()  

obj2 = ChildClass()  
