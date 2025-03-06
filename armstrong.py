def is_armstrong(number):
    temp = number
    total = 0
    num_digits = len(str(number))

    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    if total == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

num = int(input("Enter a number: "))
is_armstrong(num)
