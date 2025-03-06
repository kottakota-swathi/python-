def contains_value(arr, value):
    if value in arr:
        print(f"Array contains {value}.")
    else:
        print(f"Array does not contain {value}.")

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the value to check: "))
contains_value(numbers, target)
