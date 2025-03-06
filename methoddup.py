def remove_duplicates(arr):
    return list(set(arr))

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

unique_array = remove_duplicates(arr)

print("Array after removing duplicates:", unique_array)
