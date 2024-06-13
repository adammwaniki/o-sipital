# lib/models/medicine.py

from models.prescription import Prescription
from models.__init__ import CURSOR, CONN

class Medicine:
    all = {}

    def __init__(self, medicine_id, name, manufacturer, expiry_date, price):
        self.medicine_id = medicine_id
        self.name = name
        self.manufacturer = manufacturer
        self.expiry_date = expiry_date
        self.price = price

    def __repr__(self):
        return f"Medicine('ID: {self.medicine_id}', '{self.name}', manufacturer: '{self.manufacturer}', expiry: '{self.expiry_date}', price: '{self.price}')"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS medicines(
            id INTEGER PRIMARY KEY,
            name TEXT,
            manufacturer TEXT,
            expiry_date TEXT,
            price REAL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS medicines;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO medicines(name, manufacturer, expiry_date, price)
            VALUES (?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.manufacturer, self.expiry_date, self.price))
        CONN.commit()

        self.medicine_id = CURSOR.lastrowid  # Update medicine_id with the last inserted row id
        type(self).all[self.medicine_id] = self

    @classmethod
    def create(cls, name, manufacturer, expiry_date, price):
        medicine = cls(None, name, manufacturer, expiry_date, price)  # Initialize with None for auto-generated ID
        medicine.save()
        return medicine

    def update(self):
        sql = """
            UPDATE medicines
            SET name = ?, manufacturer = ?, expiry_date = ?, price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.manufacturer, self.expiry_date, self.price, self.medicine_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM medicines
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.medicine_id,))
        CONN.commit()

        del type(self).all[self.medicine_id]
        self.medicine_id = None

    @classmethod
    def instance_from_db(cls, row):
        medicine_id = row[0]
        medicine = cls.all.get(medicine_id)
        if medicine:
            medicine.name = row[1]
            medicine.manufacturer = row[2]
            medicine.expiry_date = row[3]
            medicine.price = row[4]
        else:
            medicine = cls(medicine_id, row[1], row[2], row[3], row[4])
            cls.all[medicine_id] = medicine
        return medicine

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM medicines
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, medicine_id):
        sql = """
            SELECT *
            FROM medicines
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (medicine_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM medicines
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def get_prescriptions(self):
        sql = """
            SELECT *
            FROM prescriptions
            WHERE medicine_id = ?
        """
        rows = CURSOR.execute(sql, (self.medicine_id,)).fetchall()
        return [Prescription.instance_from_db(row) for row in rows]
