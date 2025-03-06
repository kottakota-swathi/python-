class Student:
    def __init__(self, name, age, course):
        self.name = name  
        self.age = age  
        self.course = course  
        print("Constructor Called: Attributes Assigned")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = Student("AIthi", 22, "Computer Science")  
student1.display()  
