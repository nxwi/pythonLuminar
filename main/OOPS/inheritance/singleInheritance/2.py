# Create a parent class team leader with attributes: team_leader_name, work_block_no, company_name
# create child class employee with attributes: emp_name, id, post
# create a employee object?

class TeamLeader:
    def __init__(self, team_leader_name, work_block_no, company_name):
        self.team_leader_name = team_leader_name
        self.work_block_no = work_block_no
        self.company_name = company_name


class Employee(TeamLeader):
    def __init__(self, team_leader_name, work_block_no, company_name, emp_name, id, post):
        super().__init__(team_leader_name, work_block_no, company_name)
        self.en = emp_name
        self.id = id
        self.pt = post

    def display(self):
        print()
        print(f"Team leader name: {self.team_leader_name}")
        print(f"Work block no: {self.work_block_no}")
        print(f"Company name: {self.company_name}")
        print(f"Employee name: {self.en}")
        print(f"ID: {self.id}")
        print(f"Post: {self.pt}")


obj = Employee("John Smith", "12345", "Google",
               "Alice Doe", "123456789", "Software Engineer")
obj.display()
