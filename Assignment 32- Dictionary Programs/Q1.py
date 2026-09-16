# Assignment 32 
''' Question 1: 
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name : Ajay
Age : 35
Gender : Male
Disease : Fever
Doctor : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name : Ajay
Age : 35
Disease : Fever
Doctor : Dr. Sharma
--------------------------------

Patient ID : 102
Name : Ravi
Age : 42
Disease : Diabetes
Doctor : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101 Ajay
108 Aman
115 Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name : Ravi
Age : 68
Disease : Diabetes
Doctor : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name : Riya
Age : 4
Disease : Viral Fever
Doctor : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System

'''

n = int(input("Enter the number of patients: "))

patient = {}

for i in range(n):
    patientID = int(input("Enter patient ID: "))
    patientName = input("Enter patient Name: ")
    age = int(input("Enter the age: "))
    gender = input("Enter gender: ")
    disease = input("Enter disease: ")
    doctorName = input("Enter Doctor Name: ")

    patient[patientID] = {
        "name": patientName,
        "age": age,
        "gender": gender,
        "disease": disease,
        "doctor": doctorName
    }


while True:
    print('''
1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit
''')

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("Add a new patient:")

            patientID = int(input("Enter patient ID: "))
            patientName = input("Enter patient Name: ")
            age = int(input("Enter the age: "))
            gender = input("Enter gender: ")
            disease = input("Enter disease: ")
            doctorName = input("Enter Doctor Name: ")

            patient[patientID] = {
                "name": patientName,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctorName
            }

            print("Patient added successfully.")

        case 2:
            patientID = int(input("Enter the Patient ID: "))

            if patientID in patient:
                print("Patient Found")
                for k, v in patient.items():
                    if k == patientID:
                        print("Patient ID:", k)
                        for key, val in v.items():
                            print(key,":",val)
            else:
                print("Patient Not Found")

        case 3:
            patientID = int(input("Enter the Patient ID: "))

            if patientID in patient:
                newDisease = input("Enter new disease: ")
                patient[patientID]["disease"] = newDisease
                print("Disease updated successfully")
            else:
                print("Patient Not Found")

        case 4:
            patientID = int(input("Enter the Patient ID: "))

            if patientID in patient:
                del patient[patientID]
                print("Record deleted successfully")
            else:
                print("Patient Record Not Found")

        case 5:
            print("Display All Patients:")

            if len(patient) == 0:
                print("No patient records found.")
            else:
                for k, v in patient.items():
                    print("Patient ID:", k)
                    print("Name:", v["name"])
                    print("Age:", v["age"])
                    print("Gender:", v["gender"])
                    print("Disease:", v["disease"])
                    print("Doctor:", v["doctor"])
                    print("-" * 30)

        case 6:
            print("Total Patients:", len(patient))

        case 7:
            disease = input("Enter the disease: ")

            found = False

            for k, v in patient.items():
                if v["disease"].lower() == disease.lower():
                    print(k, v["name"])
                    found = True

            if not found:
                print("No Patient Found")

        case 8:
            if len(patient) == 0:
                print("No Patient Found")
            else:
                oldestID = max(patient, key=lambda x: patient[x]["age"])

                print("Oldest Patient:")
                print("Patient ID:", oldestID)
                print(patient[oldestID])

        case 9:
            if len(patient) == 0:
                print("No Patient Found")
            else:
                youngestID = min(patient, key=lambda x: patient[x]["age"])

                print("Youngest Patient:")
                print("Patient ID:", youngestID)
                print(patient[youngestID])

        case 10:
            print("Program exited successfully.")
            print("Thank You For Using Hospital Patient Management System.")
            break

        case _:
            print("Invalid choice. Please try again.")


    again = input("Do you want to continue (Yes/No) :")

    match again.lower():
        case "yes":
            continue

        case "no":
            break

        case __:
            print("Enter correct choice")
            break

print("Thank You For Using Hospital Patient Management System")   

