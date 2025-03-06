class OverloadExample:
    def show(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                print("Method with One Integer Parameter:", args[0])
            elif isinstance(args[0], str):
                print("Method with One String Parameter:", args[0])
        elif len(args) == 2:
            print("Method with Two Parameters of Different Types:", args[0], "and", args[1])

obj = OverloadExample()
obj.show(10)  
obj.show("AIthi")  
obj.show(20, "Python")  
