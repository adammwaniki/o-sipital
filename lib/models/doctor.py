from models.__init__ import CURSOR, CONN


class Doctor:
    def __init__(self, doctor_id, first_name, last_name, specialization, age, consultation_fees):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.age = age
        self.consultation_fees = consultation_fees
        # I'll see if the best option is to put it here or in the class
        # self.patients = []

    def __repr__(self):
        return f"Doctor {self.first_name} {self.last_name} - {self.specialization}, age: '{self.age}', fees:'{self.consultation_fees}' "