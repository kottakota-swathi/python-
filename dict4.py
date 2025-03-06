# Creating a dictionary with 5 key-value pairs
students = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David",
    "105": "Eve"
}

# Creating a nested dictionary with Student ID, Name, and Additional Info
nested_students = {
    "101": {"Name": "Alice", "Age": 20, "Grade": "A"},
    "102": {"Name": "Bob", "Age": 21, "Grade": "B"},
    "103": {"Name": "Charlie", "Age": 22, "Grade": "A"},
    "104": {"Name": "David", "Age": 20, "Grade": "C"},
    "105": {"Name": "Eve", "Age": 23, "Grade": "B"}
}

print("\nOriginal Student Dictionary:", students)
print("\nNested Student Dictionary:")

# Accessing values using a nested loop
for student_id, details in nested_students.items():
    print(f"\nStudent ID: {student_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")
