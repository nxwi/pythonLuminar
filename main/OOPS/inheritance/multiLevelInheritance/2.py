class Hospital:
    def __init__(self, h_name, loc):
        self.h_name = h_name
        self.loc = loc


class Doctor(Hospital):
    def __init__(self, h_name, loc, d_name, specialization):
        self.d_name = d_name
        self.specialization = specialization
        Hospital.__init__(self, h_name, loc)


class Patient(Doctor):
    def __init__(self, h_name, loc, d_name, specialization, p_name, token):
        self.p_name = p_name
        self.token = token
        Doctor.__init__(self, h_name, loc, d_name, specialization)

    def display(self):
        print()
        print(f"Hospital Name :{self.h_name}")
        print(f"Location :{self.loc}")
        print(f"Doctor Name :{self.d_name}")
        print(f"Specialization :{self.specialization}")
        print(f"Patient Name :{self.p_name}")
        print(f"Token No. :{self.token}")


obj = Patient("ABC Hospital", "California, USA",
              "Dr. John Smith", "Cardiology",
              "Michael Jones", "123")
obj.display()
