def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
        print(f"Updated array after removing {value}: {arr}")
    else:
        print(f"Element {value} not found in the array.")

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the element to remove: "))
remove_element(numbers, target)
