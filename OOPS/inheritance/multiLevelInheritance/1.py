class Hospital:
    def parenta(self, h_name, loc):
        self.h_name = h_name
        self.loc = loc


class Doctor(Hospital):
    def parentb(self, d_name, specialization):
        self.d_name = d_name
        self.specialization = specialization


class Patient(Doctor):
    def child(self, p_name, token):
        self.p_name = p_name
        self.token = token

    def display(self):
        print()
        print(f"Hospital Name :{self.h_name}")
        print(f"Location :{self.loc}")
        print(f"Doctor Name :{self.d_name}")
        print(f"Specialization :{self.specialization}")
        print(f"Patient Name :{self.p_name}")
        print(f"Token No. :{self.token}")


obj = Patient()
obj.parenta("ABC Hospital", "California, USA")
obj.parentb("Dr. John Smith", "Cardiology")
obj.child("Michael Jones", "123")
obj.display()
