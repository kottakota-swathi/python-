def difference_max_min(arr):
    return max(arr) - min(arr)

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

result = difference_max_min(arr)

print("Difference between largest and smallest value:", result)
