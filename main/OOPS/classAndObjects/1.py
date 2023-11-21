# Create  a class student with attributes: student_name, roll_number, department and total_score
# with static variables: school_name, school email id and location

class Student:
    school_name = "ABD School"
    school_email = "hi@abc.edu"
    location = "Unknown"

    def setval(self, student_name, roll_number, department, total_score):
        self.name = student_name
        self.rlno = roll_number
        self.dep = department
        self.score = total_score

    def display(self):
        print()
        print("School name:", Student.school_name)
        print("School email:", Student.school_email)
        print("Location:", Student.location)
        print("Student name:", self.name)
        print("Roll number:", self.rlno)
        print("Department:", self.dep)
        print("Total mark:", self.score)


std1 = Student()
std1.setval("Alex", 12, "CS", 209)
std1.display()
