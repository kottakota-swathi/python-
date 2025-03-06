def check_even_odd(n):
    switch = {
        0: "Even",
        1: "Odd"
    }
    print(f"{n} is {switch[n % 2]}.")

num = int(input("Enter a number: "))
check_even_odd(num)
