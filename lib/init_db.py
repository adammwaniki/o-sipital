# lib/init_db.py
import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Create the patients table
cursor.execute('''
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
''')

# Create the doctors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    specialty TEXT,
    phone_number TEXT,
    email TEXT
)
''')

# Create the medicines table
cursor.execute('''
CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manufacturer TEXT,
    expiry_date TEXT,
    price REAL
)
''')

# Creating a prescriptions table to handle patients treatment regimens
cursor.execute('''
CREATE TABLE IF NOT EXISTS prescriptions (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    medicine_id INTEGER,
    dosage TEXT,
    frequency TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients (id),
    FOREIGN KEY (medicine_id) REFERENCES medicines (id)
)
''') 
               

# Commit the changes and close the connection
conn.commit()
conn.close()
