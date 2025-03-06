def reverse_array(arr):
    return arr[::-1]

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

reversed_arr = reverse_array(arr)

print("Reversed Array:", reversed_arr)
