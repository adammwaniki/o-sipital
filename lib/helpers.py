from models.doctor import Doctor
from models.patient import Patient
from models.medicine import Medicine
# from models.prescription import Prescription


def exit_program():
    print("====================== Remember to take an apple a day! Goodbye! ======================")
    exit()

# Helper functions for the patients

def list_all_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

# Both name searches are case insensitive
def find_patient_by_first_name():
    first_name = input("Enter the patient's first name: ").lower()
    patient = Patient.find_by_name(first_name.lower())
    print(patient) if patient else print(f'Patient with first name {first_name} not found')

def find_patient_by_last_name():
    last_name = input("Enter the patient's last name: ").lower()
    patient = Patient.find_by_name(last_name.lower())
    print(patient) if patient else print(f'Patient with last name {last_name} not found')

def find_patient_by_id():
    id_ = input("Enter the patient's id: ")
    patient = Patient.find_by_id(id_)
    print(patient) if patient else print(f'Patient {id_} not found')

def add_patient():
    first_name = input("Enter the patient's first name: ")
    last_name = input("Enter the patient's last name: ")
    age = int(input("Enter the patient's age: "))  # Ensuring age is converted to int
    weight = float(input("Enter the patient's weight (in kg): "))  # Ensuring weight is converted to float
    height = float(input("Enter the patient's height (in cm): "))  # Ensuring height is converted to float
    phone_number = input("Enter the patient's phone number: ")
    sickness = input("Enter the patient's sickness: ")

    try:
        # Create a Patient object
        patient = Patient.create(first_name, last_name, age, weight, height, phone_number, sickness)

        # Print success message
        print(f'Success: Patient {patient.first_name} {patient.last_name} added with ID: {patient.patient_id}')
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    id_ = input("Enter the patient's id: ")
    if patient := Patient.find_by_id(id_):
        try:
            first_name = input("Enter the patient's new first name: ")
            patient.first_name = first_name
            last_name = input("Enter the patient's new last name: ")
            patient.last_name = last_name
            age = int(input("Enter the patient's new age: "))
            patient.age = age
            weight = float(input("Enter the patient's new weight: "))
            patient.weight = weight
            height = float(input("Enter the patient's new height (in cm): "))
            patient.height = height
            phone_number = input("Enter the patient's new phone number: ")
            patient.phone_number = phone_number
            sickness = input("Enter the patient's new sickness: ")
            patient.sickness = sickness

            patient.update()
            print(f'Success: {patient}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient {id_} not found')

def delete_patient():
    id_ = input("Enter the patient's id: ")
    if patient := Patient.find_by_id(id_):
        patient.delete()
        print(f'Patient {id_} deleted')
    else:
        print(f'Patient {id_} not found')

def list_patients_with_doctors():
    patients = Patient.get_all()
    for patient in patients:
        doctor = patient.get_doctor()
        doctor_info = f"{doctor.first_name} {doctor.last_name}" if doctor else "No doctor assigned"
        print(f"Patient: {patient.first_name} {patient.last_name}, Doctor: {doctor_info}")

def assign_doctor_to_patient():
    # List all patients
    list_all_patients()
    patient_id = input("Enter the patient's id you want to assign a doctor to: ")
    patient = Patient.find_by_id(patient_id)
    if not patient:
        print(f'Patient with id {patient_id} not found')
        return

    # List all doctors
    list_all_doctors()
    doctor_id = input("Enter the doctor's id you want to assign to the patient: ")
    doctor = Doctor.find_by_id(doctor_id)
    if not doctor:
        print(f'Doctor with id {doctor_id} not found')
        return

    # Assign the doctor to the patient
    try:
        patient.assign_doctor(doctor_id)
        print(f'Success: Doctor {doctor.first_name} {doctor.last_name} assigned to Patient {patient.first_name} {patient.last_name}')
    except Exception as exc:
        print(f"Error assigning doctor: {exc}")


# Helper functions for the doctors

def list_all_doctors():
    doctors = Doctor.get_all()
    for doctor in doctors:
        print(doctor)

def find_doctor_by_first_name():
    first_name = input("Enter the doctor's first name: ")
    doctor = Doctor.find_by_name(first_name)
    print(doctor) if doctor else print(f'Doctor with first name {first_name} not found')

def find_doctor_by_last_name():
    last_name = input("Enter the doctor's last name: ")
    doctor = Doctor.find_by_name(last_name)
    print(doctor) if doctor else print(f'Doctor with last name {last_name} not found')

def find_doctor_by_id():
    id_ = input("Enter the doctor's id: ")
    doctor = Doctor.find_by_id(id_)
    print(doctor) if doctor else print(f'Doctor {id_} not found')

def add_doctor():
    first_name = input("Enter the doctor's first name: ")
    last_name = input("Enter the doctor's last name: ")
    specialty = input("Enter the doctor's specialty: ")
    phone_number = input("Enter the doctor's phone number: ")
    email = input("Enter the doctor's email: ")
    try:
        doctor = Doctor.create(first_name, last_name, specialty, phone_number, email)
        print(f'Success: {doctor}')
    except Exception as exc:
        print("Error creating doctor: ", exc)

def update_doctor():
    id_ = input("Enter the doctor's id: ")
    if doctor := Doctor.find_by_id(id_):
        try:
            first_name = input("Enter the doctor's new first name: ")
            doctor.first_name = first_name
            last_name = input("Enter the doctor's new last name: ")
            doctor.last_name = last_name
            specialty = input("Enter the doctor's new specialty: ")
            doctor.specialty = specialty
            phone_number = input("Enter the doctor's new phone number: ")
            doctor.phone_number = phone_number
            email = input("Enter the doctor's new email: ")
            doctor.email = email

            doctor.update()
            print(f'Success: {doctor}')
        except Exception as exc:
            print("Error updating doctor: ", exc)
    else:
        print(f'Doctor {id_} not found')

def delete_doctor():
    id_ = input("Enter the doctor's id: ")
    if doctor := Doctor.find_by_id(id_):
        doctor.delete()
        print(f'Doctor ID: {id_} deleted')
    else:
        print(f'Doctor ID: {id_} not found')

# Helper functions for the medicines

def list_all_medicines():
    medicines = Medicine.get_all()
    for medicine in medicines:
        print(medicine)

def find_medicine_by_name():
    name = input("Enter the medicine's name: ")
    medicine = Medicine.find_by_name(name)
    print(medicine) if medicine else print(f'Medicine with name {name} not found')

def find_medicine_by_id():
    id_ = input("Enter the medicine's id: ")
    medicine = Medicine.find_by_id(id_)
    print(medicine) if medicine else print(f'Medicine {id_} not found')

def add_medicine():
    name = input("Enter the medicine's name: ")
    manufacturer = input("Enter the medicine's manufacturer: ")
    expiry_date = input("Enter the medicine's expiry date (YYYY-MM-DD): ")
    price = float(input("Enter the medicine's price: "))
    try:
        medicine = Medicine.create(name, manufacturer, expiry_date, price)
        print(f'Success: {medicine}')
    except Exception as exc:
        print("Error creating medicine: ", exc)

def update_medicine():
    id_ = input("Enter the medicine's id: ")
    if medicine := Medicine.find_by_id(id_):
        try:
            name = input("Enter the medicine's new name: ")
            medicine.name = name
            manufacturer = input("Enter the medicine's new manufacturer: ")
            medicine.manufacturer = manufacturer
            expiry_date = input("Enter the medicine's new expiry date (YYYY-MM-DD): ")
            medicine.expiry_date = expiry_date
            price = float(input("Enter the medicine's new price: "))
            medicine.price = price

            medicine.update()
            print(f'Success: {medicine}')
        except Exception as exc:
            print("Error updating medicine: ", exc)
    else:
        print(f'Medicine {id_} not found')

def delete_medicine():
    id_ = input("Enter the medicine's id: ")
    if medicine := Medicine.find_by_id(id_):
        medicine.delete()
        print(f'Medicine {id_} deleted')
    else:
        print(f'Medicine {id_} not found')

def list_patients_with_medicines():
    patients = Patient.get_all()
    for patient in patients:
        medicines = patient.get_medicines()
        if medicines:
            medicines_info = ", ".join([medicine.name for medicine in medicines])
        else:
            medicines_info = "No medicines assigned"
        print(f"Patient: {patient.first_name} {patient.last_name}, Medicines: {medicines_info}")


def assign_medicine_to_patient():
    patient_id = int(input("Enter the patient ID: "))
    medicine_id = int(input("Enter the medicine ID: "))
    dosage = input("Enter the dosage: ")
    frequency = input("Enter the frequency: ")
    
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.assign_medicine(medicine_id, dosage, frequency)
        print(f"Medicine with ID {medicine_id} assigned to patient with ID {patient_id}.")
    else:
        print(f"Patient with ID {patient_id} not found.")


"""# Prescripiton helpers

def list_all_prescriptions():
    prescriptions = Prescription.get_all()
    for prescription in prescriptions:
        print(prescription)

def add_prescription():
    patient_id = input("Enter the patient's ID: ")
    doctor_id = input("Enter the doctor's ID: ")
    medicine_id = input("Enter the medicine's ID: ")
    dosage = input("Enter the dosage: ")
    frequency = input("Enter the frequency: ")
    try:
        prescription = Prescription.create(patient_id, doctor_id, medicine_id, dosage, frequency)
        print(f'Success: {prescription}')
    except Exception as exc:
        print("Error creating prescription: ", exc)

def update_prescription():
    id_ = input("Enter the prescription's ID: ")
    if prescription := Prescription.find_by_id(id_):
        try:
            patient_id = input("Enter the new patient ID: ")
            prescription.patient_id = patient_id
            doctor_id = input("Enter the new doctor ID: ")
            prescription.doctor_id = doctor_id
            medicine_id = input("Enter the new medicine ID: ")
            prescription.medicine_id = medicine_id
            dosage = input("Enter the new dosage: ")
            prescription.dosage = dosage
            frequency = input("Enter the new frequency: ")
            prescription.frequency = frequency

            prescription.update()
            print(f'Success: {prescription}')
        except Exception as exc:
            print("Error updating prescription: ", exc)
    else:
        print(f'Prescription {id_} not found')

def delete_prescription():
    id_ = input("Enter the prescription's ID: ")
    if prescription := Prescription.find_by_id(id_):
        prescription.delete()
        print(f'Prescription {id_} deleted')
    else:
        print(f'Prescription {id_} not found')"""