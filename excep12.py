class Sample:
    def __init__(self):
        self.exists = "This field exists"

try:
    obj = Sample()
    print(obj.non_existent_field)  # Trying to access a non-existent attribute

except AttributeError:
    print("Error: No such field exists in the class!")
