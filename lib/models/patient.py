# from lib.models.medicine import Medicine
from models.prescription import Prescription
from models.__init__ import CURSOR, CONN

class Patient:

    # Dictionary of objects saved to the database
    all = {}

    def __init__(self, patient_id, first_name, last_name, age, weight, height, phone_number, sickness, doctor_id=None):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.height = height
        self.phone_number = phone_number
        self.sickness = sickness
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"Patient('ID: {self.patient_id}', '{self.first_name}', '{self.last_name}', age: '{self.age}', weight: '{self.weight}'kg, height: '{self.height}'cm, tel: '{self.phone_number}', sickness: '{self.sickness}', doctor_id: '{self.doctor_id}')"
    
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
    
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value

    def save(self):
        """ Save the Patient instance to the database """
        sql = """
            INSERT INTO patients(first_name, last_name, age, weight, height, phone_number, sickness, doctor_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.weight, self.height, self.phone_number, self.sickness, self.doctor_id))
        CONN.commit()

        self.patient_id = CURSOR.lastrowid
        type(self).all[self.patient_id] = self

    def update(self):
        """Update the table row corresponding to the current Patient instance."""
        sql = """
            UPDATE patients
            SET first_name = ?, last_name = ?, age = ?, weight = ?, height = ?, phone_number = ?, sickness = ?, doctor_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.weight, self.height, self.phone_number, self.sickness, self.doctor_id, self.patient_id))
        CONN.commit()

    def assign_doctor(self, doctor_id):
        """Assign a doctor to the patient."""
        self.doctor_id = doctor_id
        self.update()

    def get_doctor(self):
        """Return the doctor associated with this patient."""
        from models.doctor import Doctor
        if self.doctor_id is None:
            return None
        sql = """
            SELECT * FROM doctors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.doctor_id,))
        row = CURSOR.fetchone()
        return Doctor.instance_from_db(row) if row else None

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of the Patient instances """
        sql = """
            CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            phone_number TEXT,
            sickness TEXT,
            doctor_id INTEGER,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists the attributes of the Patient instances """
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, first_name, last_name, age, weight, height, phone_number, sickness):
        """ Initialize a new Patient instance and save the object to the database """
        # Create the Patient instance without specifying patient_id
        patient = cls(None, first_name, last_name, age, weight, height, phone_number, sickness)
        
        # Save the patient to the database
        patient.save()
        
        # Return the created patient instance with the actual primary key assigned by the database
        return patient

    def delete(self):
        """Delete the table row corresponding to the current Patient instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM patients
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.patient_id,))
        CONN.commit()

        # Delete the dictionary entry using patient_id as the key
        del type(self).all[self.patient_id]

        # Set the patient_id to None
        self.patient_id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Patient object having the attribute values from the table row."""

        # Extract values from the row
        if row is None:
            return None

        patient_id = row[0]
        first_name = row[1]
        last_name = row[2]
        age = row[3]
        weight = row[4]
        height = row[5]
        phone_number = row[6]
        sickness = row[7]
        doctor_id = row[8]  # Fetch doctor_id from database

        patient = cls.all.get(patient_id)
        if patient:
            patient.first_name = first_name
            patient.last_name = last_name
            patient.age = age
            patient.weight = weight
            patient.height = height
            patient.phone_number = phone_number
            patient.sickness = sickness
            patient.doctor_id = doctor_id  # Update doctor_id if already exists
        else:
            patient = cls(patient_id, first_name, last_name, age, weight, height, phone_number, sickness, doctor_id)
            cls.all[patient_id] = patient

        return patient

    @classmethod
    def get_all(cls):
        """Return a list containing a Patient object per row in the table"""
        sql = """
            SELECT *
            FROM patients
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, patient_id):
        """Return a Patient object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM patients
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (patient_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Patient object corresponding to the first table row matching specified name"""
        # Converting the name to lowercase and adding wildcards to handle partial matches
        name = '%' + name.lower() + '%'  
        sql = """
            SELECT *
            FROM patients
            WHERE LOWER(first_name) LIKE ?
               OR LOWER(last_name) LIKE ?
        """
        rows = CURSOR.execute(sql, (name, name)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None

    

    def get_prescriptions(self):
        return Prescription.find_by_patient_id(self.id)

    '''def get_medicines(self):
        prescriptions = self.get_prescriptions()
        return [prescription.medicine for prescription in prescriptions]'''
    
    def assign_medicine(self, medicine_id, dosage, frequency):
        Prescription.create(self.patient_id, medicine_id, dosage, frequency)

    def get_medicines(self):
        """Return a list of medicines assigned to the patient."""
        prescriptions = Prescription.find_by_patient_id(self.patient_id)
        return [prescription.get_medicine() for prescription in prescriptions]
    
'''   def get_medicines(self):
        sql = """
            SELECT m.*
            FROM medicines m
            JOIN prescriptions p ON m.id = p.medicine_id
            WHERE p.patient_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Medicine.instance_from_db(row) for row in rows] if rows else []'''

    
