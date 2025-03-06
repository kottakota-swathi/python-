class MyException(Exception):
    def __init__(self, message):
        self.message = message

def validate_age(age):
    if age < 18:
        raise MyException("Age must be 18 or above!")
    print("Valid age:", age)

age = int(input("Enter your age: "))
validate_age(age)
