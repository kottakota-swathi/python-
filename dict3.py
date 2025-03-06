# Creating a dictionary with 5 key-value pairs
students = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David",
    "105": "Eve"
}

print("\nStudent Dictionary:", students)

# Accessing values dynamically
student_id = input("\nEnter Student ID to get the Name: ")

if student_id in students:
    print(f"\nStudent Name: {students[student_id]}")
else:
    print("\nError: Student ID not found!")
