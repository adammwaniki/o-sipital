# lib/cli.py

import sqlite3

from helpers import (
    exit_program,
    list_all_patients,
    find_patient_by_first_name,
    find_patient_by_last_name,
    find_patient_by_id,
    add_patient,
    update_patient,
    delete_patient,
    list_all_doctors,
    find_doctor_by_first_name,
    find_doctor_by_last_name,
    find_doctor_by_id,
    add_doctor,
    update_doctor,
    delete_doctor,
    list_all_medicines,
    find_medicine_by_name,
    find_medicine_by_id,
    add_medicine,
    update_medicine,
    delete_medicine,
    list_patients_with_doctors,
    assign_doctor_to_patient,
    list_patients_with_medicines,
    list_all_prescriptions,
    add_prescription,
    update_prescription,
    delete_prescription,
)

DATABASE_PATH = 'hospital.db'

def main():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_patients()
        elif choice == "2":
            find_patient_by_first_name()
        elif choice == "3":
            find_patient_by_last_name()
        elif choice == "4":
            find_patient_by_id()
        elif choice == "5":
            add_patient()
        elif choice == "6":
            update_patient()
        elif choice == "7":
            delete_patient()
        elif choice == "8":
            list_all_doctors()
        elif choice == "9":
            find_doctor_by_first_name()
        elif choice == "10":
            find_doctor_by_last_name()
        elif choice == "11":
            find_doctor_by_id()
        elif choice == "12":
            add_doctor()
        elif choice == "13":
            update_doctor()
        elif choice == "14":
            delete_doctor()
        elif choice == "15":
            list_all_medicines()
        elif choice == "16":
            find_medicine_by_name()
        elif choice == "17":
            find_medicine_by_id()
        elif choice == "18":
            add_medicine()
        elif choice == "19":
            update_medicine()
        elif choice == "20":
            delete_medicine()
        elif choice == '21':
            list_patients_with_doctors()
        elif choice == '22':
            assign_doctor_to_patient()
        elif choice == '23':
            list_patients_with_medicines()
        elif choice == '24':
            list_all_prescriptions()
        elif choice == '25':
            add_prescription()
        elif choice == '26':
            update_prescription()
        elif choice == '27':
            delete_prescription()
        else:
            print("Invalid choice")
    # conn.close() # this doesn't seem to be necessary

def menu():
    print("\nHospital Management System")
    print("0. Exit the program")
    print("1. Show a list of all patients")
    print("2. Find a patient by first name")
    print("3. Find a patient by last name")
    print("4. Find a patient by ID")
    print("5. Add a new patient record")
    print("6. Update patient records")
    print("7. Delete a patient from the database")
    print("8. Show a list of all the doctors")
    print("9. Find a doctor by first name")
    print("10. Find a doctor by last name")
    print("11. Find a doctor by id")
    print("12. Add a new doctor")
    print("13. Update doctor records")
    print("14. Delete a doctor from the database")
    print("15. Show a list of all the medicines")
    print("16. Find a medicine by its name")
    print("17. Find a medicine by its id")
    print("18. Add a medicine")
    print("19. Update a medicine")
    print("20. Delete a medicine")
    print("21. List patients with their assigned doctors")
    print("22. Assign a doctor to a patient")
    print("23. List patients with their assigned medicines")
    print("24. List all prescriptions")
    print("25. Add a new prescription")
    print("26. Update a prescription")
    print("27. Delete a prescription")

if __name__ == "__main__":
    main()
