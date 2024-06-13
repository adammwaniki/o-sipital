# lib/models/doctor.py

from models.__init__ import CURSOR, CONN
from models.prescription import Prescription

class Doctor:
    all = {}

    def __init__(self, doctor_id, first_name, last_name, specialty, phone_number, email):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return f"Doctor('ID: {self.doctor_id}', '{self.first_name}', '{self.last_name}', specialty: '{self.specialty}', tel: '{self.phone_number}', email: '{self.email}')"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS doctors(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            specialty TEXT,
            phone_number TEXT,
            email TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS doctors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO doctors(first_name, last_name, specialty, phone_number, email)
            VALUES (?, ?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.specialty, self.phone_number, self.email))
        CONN.commit()

        self.doctor_id = CURSOR.lastrowid  # Update doctor_id with the last inserted row id
        type(self).all[self.doctor_id] = self

    @classmethod
    def create(cls, first_name, last_name, specialty, phone_number, email):
        doctor_id = None  # Let the database generate the id
        doctor = cls(doctor_id, first_name, last_name, specialty, phone_number, email)
        doctor.save()
        return doctor

    def update(self):
        sql = """
            UPDATE doctors
            SET first_name = ?, last_name = ?, specialty = ?, phone_number = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.specialty, self.phone_number, self.email, self.doctor_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM doctors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.doctor_id,))
        CONN.commit()

        del type(self).all[self.doctor_id]
        self.doctor_id = None

    @classmethod
    def instance_from_db(cls, row):
        doctor_id = row[0]
        doctor = cls.all.get(doctor_id)
        if doctor:
            doctor.first_name = row[1]
            doctor.last_name = row[2]
            doctor.specialty = row[3]
            doctor.phone_number = row[4]
            doctor.email = row[5]
        else:
            doctor = cls(doctor_id, row[1], row[2], row[3], row[4], row[5])
            cls.all[doctor_id] = doctor
        return doctor

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM doctors
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM doctors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        # case insensitive search with allowance for partial matches
        name = '%' + name.lower() + '%'
        sql = """
            SELECT *
            FROM doctors
             WHERE LOWER(first_name) LIKE ?
               OR LOWER(last_name) LIKE ?
        """
        rows = CURSOR.execute(sql, (name, name)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None
    
    def get_prescriptions(self):
        sql = """
            SELECT *
            FROM prescriptions
            WHERE doctor_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Prescription.instance_from_db(row) for row in rows]
