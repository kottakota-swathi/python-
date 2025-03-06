class OverloadExample:
    def show(self, *args):
        if len(args) == 1:
            print("Method with One Parameter:", args[0])
        elif len(args) == 2:
            print("Method with Two Parameters:", args[0], "and", args[1])

obj = OverloadExample()
obj.show(10)  
obj.show(20, 30)  
