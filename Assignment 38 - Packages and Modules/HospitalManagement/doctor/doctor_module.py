'''
Doctor Management Package

Create a package named "doctor".

Create module:
doctor_module.py


Implement the following functions:


a) add_doctor()

Take doctor details:

- Doctor ID
- Doctor Name
- Specialization
- Experience
- Consultation Fees


Store doctor information using list and dictionary.


b) display_doctors()

Display all doctor details.

'''

doctors = []

def add_doctor(): 
    doctor = {}

    doctor["Doctor ID"] = input("Enter Doctor ID : ")
    doctor["Doctor Name"] = input("Enter Doctor Name : ")
    doctor["Specialization"] = input("Enter Specialization : ")
    doctor["Experience"] = input("Enter Experience : ")
    doctor["Consultation Fees"] = input("Enter Consultation Fees : ")

    doctors.append(doctor)

    print("\nDoctor added successfully!")


def display_doctors():
    if len(doctors)==0:
        print("\nNo Doctor Added ")

    else:
        print("\n                  Doctor Details : ")

        for d in doctors:
            print("Doctor ID :", d["Doctor ID"])
            print("Doctor Name :", d["Doctor Name"])
            print("Specialization :", d["Specialization"])
            print("Experience :", d["Experience"])
            print("Consultation Fees :", d["Consultation Fees"])
            print()