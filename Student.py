class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def show(self):
        print("Name:",self.name,"\nRoll no:",self.roll_no)
s=Student("Vyshali",21)
s.show()