class Student:

    def __init__(self, student_name, roll_number, department):
        self.name = student_name
        self.rlno = roll_number
        self.dep = department

    def display(self):
        print()
        print("Student name:", self.name)
        print("Roll number:", self.rlno)
        print("Department:", self.dep)


std1 = Student("Alex", 12, "CS")
std1.display()

std2 = Student("John", 13, "CS")
std2.display()
