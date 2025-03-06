# Creating a dictionary with 5 key-value pairs
students = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David",
    "105": "Eve"
}

print("\nOriginal Student Dictionary:", students)

# Updating values dynamically
student_id = input("\nEnter Student ID to update: ")
new_name = input("Enter New Student Name: ")

if student_id in students:
    students[student_id] = new_name  # Updating value
    print("\nUpdated Student Dictionary:", students)
else:
    print("\nError: Student ID not found!")
