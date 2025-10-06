class Student:
    """
    Represents a student with a name, age, and a list of marks.
    Provides methods to display details and calculate total marks.
    """
    def __init__(self, name, age, marks):
        """
        Initializes a Student instance.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            marks (list of int or float): The marks obtained by the student.
        """
        self.name = name
        self.age = age
        self.marks = marks
    def details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")

    def total_marks(self):
        """
        Returns the total of the student's marks.

        Returns:
            int or float: The sum of the marks.
        """
        return sum(self.marks)
        # Example function call
student = Student("Alice", 20, [85, 90, 78])
student.details()
print(f"Total Marks: {student.total_marks()}")
