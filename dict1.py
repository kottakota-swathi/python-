students = {}  # Creating an empty dictionary

# Adding key-value pairs dynamically
for _ in range(5):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    students[student_id] = student_name  # Adding to dictionary

print("\nStudent Dictionary:", students)  # Display the dictionary
