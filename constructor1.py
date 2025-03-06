class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print("One-Argument Constructor Called with:", arg1)
        else:
            print("Two-Argument Constructor Called with:", arg1, "and", arg2)

class MainClass:
    obj1 = MyClass()
    obj2 = MyClass("AIthi")
    obj3 = MyClass("AIthi", 2025)
