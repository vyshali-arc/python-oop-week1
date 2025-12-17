class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# taking input from user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

student = Student(name, roll_no, marks)
student.display()
