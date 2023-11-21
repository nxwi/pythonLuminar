class Business:
    def __init__(self, b_name, loc):
        self.b_name = b_name
        self.loc = loc


class Manager:
    def __init__(self, m_name, department):
        self.m_name = m_name
        self.department = department


class Customer(Business, Manager):
    def __init__(self, b_name, loc, m_name, department, c_name, token):
        self.c_name = c_name
        self.token = token
        Business.__init__(self, b_name, loc)
        Manager.__init__(self, m_name, department)

    def display(self):
        print()
        print(f"Business Name : {self.b_name}")
        print(f"Location : {self.loc}")
        print(f"Manager Name : {self.m_name}")
        print(f"Department : {self.department}")
        print(f"Customer Name : {self.c_name}")
        print(f"Token No. : {self.token}")


customer1 = Customer("Google", "Mountain View, California, USA",
                     "Sundar Pichai", "Technology",
                     "John Doe", "456")
customer1.display()

customer2 = Customer("Amazon", "Seattle, Washington, USA",
                     "Andy Jassy", "Retail",
                     "Jane Doe", "789")
customer2.display()

customer3 = Customer("Microsoft", "Redmond, Washington, USA",
                     "Satya Nadella", "Software",
                     "David Smith", "101112")
customer2.display()
