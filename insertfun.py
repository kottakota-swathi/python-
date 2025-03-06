def insert_element(arr, element, position):
    arr.insert(position, element)
    return arr

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

element = int(input("Enter the element to insert: "))
position = int(input("Enter the position (0-based index): "))

updated_array = insert_element(arr, element, position)

print("Updated Array:", updated_array)
