class Univ:
    def univ(self, univ_name):
        self.univ_name = univ_name


class College(Univ):
    def college(self, clg_name, loc):
        self.clg_name = clg_name
        self.loc = loc


class Branch(Univ):
    def branch(self, branch_name):
        self.branch_name = branch_name


class Student(College, Branch):
    def student(self, stu_name, reg_no):
        self.stu_name = stu_name
        self.reg_no = reg_no

    def display(self):
        print()
        print(f"University Name: {self.univ_name}")
        print(f"College Name: {self.clg_name}")
        print(f"Branch Name: {self.branch_name}")
        print(f"Student Name: {self.stu_name}")
        print(f"Registration Number: {self.reg_no}")


stu1 = Student()
stu1.univ("MIT")
stu1.college("School of Engineering", "Cambridge, MA")
stu1.branch("Computer Science")
stu1.student("John Doe", "12345678")
stu1.display()
