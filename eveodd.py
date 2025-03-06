def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

even_count, odd_count = count_even_odd(arr)

print("Number of Even Numbers:", even_count)
print("Number of Odd Numbers:", odd_count)
