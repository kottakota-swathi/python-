class OverloadExample:
    def show(self, value):
        if isinstance(value, int):
            print("Method with Integer Parameter:", value)
        elif isinstance(value, str):
            print("Method with String Parameter:", value)

obj = OverloadExample()
obj.show(10)  
obj.show("AIthi")  
