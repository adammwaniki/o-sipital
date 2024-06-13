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
    assign_medicine_to_patient,
)

DATABASE_PATH = 'hospital.db'

def main():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    while True:
        main_menu()
        main_choice = input("> ").strip().upper()
        
        if main_choice == 'A':
            patients_menu()
        elif main_choice == 'B':
            doctors_menu()
        elif main_choice == 'C':
            medicines_menu()
        elif main_choice == 'D':
            exit_program()
        else:
            print("Invalid choice. Please choose A, B, C, or D.")

def main_menu():
    print("=====================Hospital Management System=====================")
    print("               A. Patients")
    print("               B. Doctors")
    print("               C. Medicines")
    print("               D. Exit")

def patients_menu():
    while True:
        print("=====================Patients Menu=====================")
        print("             1. Show a list of all patients")
        print("             2. Find a patient by first name")
        print("             3. Find a patient by last name")
        print("             4. Find a patient by ID")
        print("             5. Add a new patient record")
        print("             6. Update patient records")
        print("             7. Delete a patient from the database")
        print("             8. Show a list of patients and their doctors")
        print("             9. Assign a doctor to a patient")
        print("             0. Back to main menu")
        
        choice = input("> ").strip()
        
        if choice == "1":
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
            list_patients_with_doctors()
        elif choice == "9":
            assign_doctor_to_patient()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

def doctors_menu():
    while True:
        print("=====================Doctors Menu=====================")
        print("             1. Show a list of all the doctors")
        print("             2. Find a doctor by first name")
        print("             3. Find a doctor by last name")
        print("             4. Find a doctor by id")
        print("             5. Add a new doctor")
        print("             6. Update doctor records")
        print("             7. Delete a doctor from the database")
        print("             0. Back to main menu")
        
        choice = input("> ").strip()
        
        if choice == "1":
            list_all_doctors()
        elif choice == "2":
            find_doctor_by_first_name()
        elif choice == "3":
            find_doctor_by_last_name()
        elif choice == "4":
            find_doctor_by_id()
        elif choice == "5":
            add_doctor()
        elif choice == "6":
            update_doctor()
        elif choice == "7":
            delete_doctor()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

def medicines_menu():
    while True:
        print("=====================Medicines Menu=====================")
        print("             1. Show a list of all the medicines")
        print("             2. Find a medicine by its name")
        print("             3. Find a medicine by its id")
        print("             4. Add a medicine")
        print("             5. Update a medicine")
        print("             6. Delete a medicine")
        print("             7. Assign a medicine prescription to a patient")
        print("             0. Back to main menu")
        
        choice = input("> ").strip()
        
        if choice == "1":
            list_all_medicines()
        elif choice == "2":
            find_medicine_by_name()
        elif choice == "3":
            find_medicine_by_id()
        elif choice == "4":
            add_medicine()
        elif choice == "5":
            update_medicine()
        elif choice == "6":
            delete_medicine()
        elif choice == "7":
            assign_medicine_to_patient()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
