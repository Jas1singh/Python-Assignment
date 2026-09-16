'''Requirements:

1. Patient Management Package

Create a package named "patient".

Create module:
patient_module.py


Implement the following functions:

a) add_patient()

Take patient details from user:

- Patient ID
- Patient Name
- Age
- Gender
- Disease
- Mobile Number


Store patient information using list and dictionary.


b) display_patients()

Display all registered patients.


c) search_patient()

Search patient details using Patient ID.
'''

patients = []


def add_patient():
    patient = {}

    patient["Patient ID"] = input("Enter Patient ID : ")
    patient["Patient Name"] = input("Enter Patient Name : ")
    patient["Age"] = int(input("Enter Age : "))
    patient["Gender"] = input("Enter Gender : ")
    patient["Disease"] = input("Enter Disease : ")
    patient["Mobile Number"] = input("Enter Mobile Number : ")

    patients.append(patient)

    print("\nPatient added successfully!")


def display_patients():
    if len(patients)!=0:
        print("\n                 Patient Details")

        for p in patients:
            print("Patient ID :", p["Patient ID"])
            print("Patient Name :", p["Patient Name"])
            print("Age :", p["Age"])
            print("Gender :", p["Gender"])
            print("Disease :", p["Disease"])
            print("Mobile Number :", p["Mobile Number"])
            print()
    else:
        print("\nNo Patient Added!!")

def search_patient():
    if len(patients)!=0:
        pid = input("Enter Patient ID to search : ")

        found = False

        for p in patients:
            if p["Patient ID"] == pid:
                print("\n Patient Found :")
                print("Patient ID :", p["Patient ID"])
                print("Patient Name :", p["Patient Name"])
                print("Age :", p["Age"])
                print("Gender :", p["Gender"])
                print("Disease :", p["Disease"])
                print("Mobile Number :", p["Mobile Number"])

                found = True
                break

            if found == False:
                print("\nPatient not found.")

    else:
        print("\nNo Patient Added Yet !!")




# P = []
# def add_patient():
#     PatientID = int(input("Enter Patient ID : "))
#     PatientName = input("Enter Patient Name : ")
#     Age = int(input("Enter Age : "))
#     Gender = input("Enter Gender : ")
#     Disease = input("Enter Disease : ")
#     MobileNumber = int(input("Enter Mobile Number: "))

#     P.append([PatientID,PatientName,Age,Gender,Disease,MobileNumber])

#     print("\nPatient added successfully")

# def display_patients():
#     for i in P:
#         print(i)

# def search_patient():
#     pID = int(input("\nEnter patient ID : "))

#     for i in P:
#         if pID==i[0]:
#             print("\nPatient Found : ")
#             print(i)