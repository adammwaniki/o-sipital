#lib/models/patients.py
from models.__init__ import CURSOR, CONN


class Patient:
    def __init__(self, patient_id, first_name, last_name, age, weight, height, phone_number, sickness):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.height = height
        self.phone_number = phone_number
        self.sickness = sickness
        # I want to see if I can link the foreign id here for the doctors that belong to a patient
        # self.doctor_id = None

    def __repr__(self):
        return f"Patient('ID: {self.patient_id}', '{self.first_name}', '{self.last_name}', age: '{self.age}', weight: '{self.weight}'kg, height: '{self.height}'cm, tel: '{self.phone_number}', sickness: '{self.sickness}')"
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and len(value):
            self._first_name = value
        else:
            raise ValueError("First name must be a non-empty string")
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and len(value):
            self._last_name = value
        else:
            raise ValueError("Last name must be a non-empty string")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer")
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if isinstance(value, float) and value > 0:
            self._weight = value
        else:
            raise ValueError("Weight must be a positive float")
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if isinstance(value, float) and value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive float in centimeters")
        
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        if isinstance(value, str) and len(value) == 10 and value.isdigit():
            self._phone_number = value
        else:
            raise ValueError("Phone number must be a 10-digit string")
        
    @property
    def sickness(self):
        return self._sickness
    
    @sickness.setter
    def sickness(self, value):
        if isinstance(value, str) and len(value):
            self._sickness = value
        else:
            raise ValueError("Sickness must be a non-empty string")
        

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of the Patient instances """
        sql = """
            CREATE TABLE IF NOT EXISTS pat"""
