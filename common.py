def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

n1 = int(input("Enter the number of elements in the first array: "))
arr1 = [int(input(f"Enter element {i+1}: ")) for i in range(n1)]

n2 = int(input("Enter the number of elements in the second array: "))
arr2 = [int(input(f"Enter element {i+1}: ")) for i in range(n2)]

common_values = find_common_values(arr1, arr2)

print("Common Values:", common_values if common_values else "No common values found")
