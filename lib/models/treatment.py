from models.__init__ import CURSOR, CONN
from models.patient import Patient


class Treatment:
    def __init__(self, treatment_id, medicine_name, patient_id, medicine_dosage, treatment_price):
        self.treatment_id = treatment_id
        self.medicine_name = medicine_name
        self.patient_id = patient_id
        self.medicine_dosage = medicine_dosage
        self.treatment_price = treatment_price
        # self.patient = Patient.get_patient_by_id(patient_id)
        # self.save_to_db()