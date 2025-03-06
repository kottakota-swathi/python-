def sum_of_array(arr):
    return sum(arr)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of array:", sum_of_array(numbers))
