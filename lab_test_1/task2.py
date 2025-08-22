# Student class definition
class Student:
    def __init__(self, name, roll_no, marks):
        # Initialize student attributes
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        # Display student details and grade
        print("Student Details:")
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.marks}")

        # Determine grade based on marks
        if 90 <= self.marks <= 100:
            grade = "A+"
        elif 75 <= self.marks < 90:
            grade = "A"
        elif 60 <= self.marks < 75:
            grade = "B"
        elif 50 <= self.marks < 60:
            grade = "C"
        else:
            grade = "F (Fail)"

        print(f"Grade   : {grade}")

# Take input from the user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Please enter marks in the range 0-100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for marks.")

# Create Student object and display details
student = Student(name, roll_no, marks)
student.display_details()

