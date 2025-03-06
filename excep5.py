class CustomError(Exception):
    def __init__(self, message):
        self.message = message

def check_number(num):
    if num < 0:
        raise CustomError("Negative numbers are not allowed!")
    print("Valid number:", num)

num = int(input("Enter a number: "))
check_number(num)  
