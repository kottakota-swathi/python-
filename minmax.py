def find_min_max(arr):
    return min(arr), max(arr)

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

minimum, maximum = find_min_max(arr)

print("Minimum Value:", minimum)
print("Maximum Value:", maximum)
