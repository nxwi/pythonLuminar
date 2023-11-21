# Create a parent class team leader with attributes: team_leader_name, work_block_no, company_name
# create child class employee with attributes: emp_name, id, post
# create a employee object?

class TeamLeader:
    def parentfun(self, team_leader_name, work_block_no, company_name):
        self.tln = team_leader_name
        self.wbn = work_block_no
        self.cn = company_name


class Employee(TeamLeader):
    def childfun(self, emp_name, id, post):
        self.en = emp_name
        self.id = id
        self.pt = post

    def display(self):
        print()
        print(f"Team leader name: {self.tln}")
        print(f"Work block no: {self.wbn}")
        print(f"Company name: {self.cn}")
        print(f"Employee name: {self.en}")
        print(f"ID: {self.id}")
        print(f"Post: {self.pt}")


obj = Employee()
obj.parentfun("John Smith", "12345", "Google")
obj.childfun("Alice Doe", "123456789", "Software Engineer")
obj.display()
