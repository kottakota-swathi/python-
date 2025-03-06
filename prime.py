def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime number.")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return

    print(f"{n} is a prime number.")

num = int(input("Enter a number: "))
is_prime(num)
