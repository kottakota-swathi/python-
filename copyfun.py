def copy_array(source_array):
    return source_array[:]

n = int(input("Enter the number of elements: "))
original = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

copied = copy_array(original)

print("Original Array:", original)
print("Copied Array:", copied)
