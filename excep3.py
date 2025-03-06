class Example:
    def throw_exception(self):
        raise Exception("Manual Exception Raised")

obj = Example()
obj.throw_exception()  # This will terminate the program
