def find_duplicates(arr):
    duplicates = set()
    seen = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

duplicates = find_duplicates(arr)

print("Duplicate Values:", duplicates if duplicates else "No duplicates found")
