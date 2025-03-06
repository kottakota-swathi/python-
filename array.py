def contains_elements(arr, elem1=12, elem2=23):
    return elem1 in arr and elem2 in arr

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

if contains_elements(arr):
    print("The array contains both 12 and 23.")
else:
    print("The array does not contain both 12 and 23.")
