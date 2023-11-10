class Hospital:
    def __init__(self, h_name, loc):
        self.h_name = h_name
        self.loc = loc


class Doctor:
    def __init__(self, d_name, specialization):
        self.d_name = d_name
        self.specialization = specialization


class Patient(Hospital, Doctor):
    def __init__(self, h_name, loc, d_name, specialization, p_name, token):
        Hospital.__init__(self, h_name, loc)
        Doctor.__init__(self, d_name, specialization)
        self.p_name = p_name
        self.token = token

    def display(self):
        print()
        print(f"Hospital Name : {self.h_name}")
        print(f"Location : {self.loc}")
        print(f"Doctor Name : {self.d_name}")
        print(f"Specialization : {self.specialization}")
        print(f"Patient Name : {self.p_name}")
        print(f"Token No. : {self.token}")


ptn1 = Patient("ABC Hospital", "California, USA",
              "Dr. John Smith", "Cardiology",
              "Michael Jones", "123")
ptn1.display()
ptn1 = Patient("XYZ Hospital", "New York, USA",
              "Dr. Jane Doe", "Surgery",
              "Mary Brown", "456")
ptn1.display()
