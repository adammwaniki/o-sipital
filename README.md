# HOSPITAL MANAGEMENT SYSTEM (HMS)

HMS is a CLI - based application

## Description

The primary purpose of this CLI - based system is to provide hospital management staff with an simple alternative to physical record keeping.
The system allows users to perform various operations such as:

- Registering patients

- Updating and deleting patient records

- Viewing patient records

- Registering new doctors

- Updating and deleting doctor records

- Viewing doctor details

- Adding new medicines to the registry

- Updating, deleting and viewing medicine records

- Assigning doctors to patients

- Assigning medicines to patients

### Dependencies

- Python 3.8 or higher installed on your machine

- You can install Python from the official Python website: ([https](https://www.python.org/downloads/))

- This project requires you to have Visual Studio Code or any other text editor installed on your machine.

- A working internet connection

#### Installing

- Clone the repository from Github onto your device

- Open your terminal/command prompt and navigate to the directory where you cloned the repository.

- Run the command `pipenv install` to install dependencies for python virtual environment. This will help prevent conflicts with your machine.

- Run the command `pipenv shell` to activate the virtual environment.

- Run the command `python lib/init_db.py` to initialize the application's database.

- Run the command `python lib/cli.py` to start the application.

- Feel free to navigate intuitively through the app

### Navigating Through The App

The HMS provides a user with 3 main routes to navigate through i.e. Patients, Doctors and Medicines

* Patients:

    * Show a list of all patients
     
    * Register a new patient
     
    * Search for a patient by first name, last name or ID
     
    * Update patient records
     
    * Show a list of patients that have been assigned doctors
     
    * Assign doctors to patients

* Doctors:
    * Show a list of all doctors
     
    * Register a new doctor
     
    * Search for a doctor by first name, last name or ID
     
    * Update doctor records
     
    * Delete doctor records

* Medicines:
    * Show a list of all medicines
     
    * Register a new medicine
     
    * Search for a doctor by name or ID
     
    * Update doctor records
     
    * Delete doctor records

    * Assign a medicine prescription to a patient


## Help

* If you face any trouble, please submit a ticket on GitHub with details about what went wrong. Include all relevant error messages and screenshots.

* Feel free to ask for help! You can do so by reaching out via email([email](adamndegwa@protonmail.com))


## Authors

Contributors names and contact info

* **Adam Mwaniki** - ([https](https://github.com/adammwaniki))