# Create a class
# doctor_details with attributes : doc_name, specialization
# patient with attributes : patient_name, token_number


class Doctor:
    def __init__(self, doc_name, specialization):
        self.doc_name = doc_name
        self.specialization = specialization


class Patient(Doctor):
    def __init__(self, doc_name, specialization, p_name, token):
        super().__init__(doc_name, specialization)
        self.p_name = p_name
        self.token = token

    def display(self):
        print()
        print(f"Doctor Name :{self.doc_name}")
        print(f"Specialization :{self.specialization}")
        print(f"Patient Name :{self.p_name}")
        print(f"Token No. :{self.token}")


obj = Patient("Dr. John Smith",
              "Cardiology",
              "Michael Jones",
              "123")
obj.display()
