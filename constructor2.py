class SuperClass:
    def __init__(self, arg1=None):
        if arg1 is None:
            print("SuperClass: Default Constructor Called")
        else:
            print("SuperClass: Argument Constructor Called with:", arg1)

class ChildClass(SuperClass):
    def __init__(self, arg1=None):
        if arg1 is None:
            super().__init__()  
            print("ChildClass: Default Constructor Called")
        else:
            super().__init__(arg1)  
            print("ChildClass: Argument Constructor Called with:", arg1)

obj1 = ChildClass()  
obj2 = ChildClass("AIthi")  
