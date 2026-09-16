# Assignment 38 - Packages and Modules
'''
Create main.py file.

Create a menu-driven program.


Menu:

========== Hospital Management System ==========

1. Add Patient

2. Display Patients

3. Search Patient

4. Add Doctor

5. Display Doctors

6. Book Appointment

7. Show Appointments

8. Generate Bill

9. Exit


According to user choice call the required functions from packages.
'''

from patient import patient_module
from doctor import doctor_module
from appointment import appointment_module
from billing import billing_module

while True:
    print('''\n ========== Hospital Management System ==========

1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit \n''')

    choice = int(input("Enter your choice : "))
    match choice:
        case 1:
            patient_module.add_patient()

        case 2:
            patient_module.display_patients()
    
        case 3:
            patient_module.search_patient()

        case 4:
            doctor_module.add_doctor()

        case 5:
            doctor_module.display_doctors()

        case 6:
            appointment_module.book_appointment()

        case 7:
            appointment_module.show_appointments()

        case 8:
            Patient_ID = int(input("Enter Patient ID : "))
            Consultation_Charges = int(input("Enter Calculation Charges"))
            Medicine_Cost = int(input("Enter Medicine Cost"))
            Test_Charges = int(input("Enter Test Charges"))

            billing_module.generate_bill(Patient_ID,Consultation_Charges,Medicine_Cost,Test_Charges)

        case 9:
            print("Exit...")
            break

        case _:
            print("Invalid Choice !!")
           