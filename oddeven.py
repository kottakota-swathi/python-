def print_odd_even():
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))

    print("\nEven Numbers:")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")

    print("\n\nOdd Numbers:")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, end=" ")

# Calling the function
print_odd_even()

