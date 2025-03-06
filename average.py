def average_of_array(arr):
    return sum(arr) / len(arr) if len(arr) > 0 else 0

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average of array:", average_of_array(numbers))
