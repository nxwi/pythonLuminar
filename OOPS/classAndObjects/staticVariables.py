class Employees:
    company_name = "TCS"

    def setval(self, name, id, salary, designation):
        self.nm = name
        self.id = id
        self.sl = salary
        self.ds = designation

    def display(self):
        print()
        print("Company name:", Employees.company_name)
        print("Name:", self.nm)
        print("ID:", self.id)
        print("Salary:", self.sl)
        print("Designation:", self.ds)


obj1 = Employees()
obj1.setval("Alex", 123, 20000, "Tester")
obj1.display()

obj2 = Employees()
obj2.setval("Sam", 124, 35000, "Designer")
obj2.display()
