def second_largest(arr):
    first, second = float('-inf'), float('-inf')

    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else "No second largest number"

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

result = second_largest(arr)

print("Second Largest Number:", result)
