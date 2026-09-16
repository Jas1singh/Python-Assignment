# Assignment 29 
''' Question 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
'''

from collections import namedtuple

n = int(input("Enter no. of Students :"))

patient = namedtuple("Patient",["PatientID","Name","Age","Disease"])

Pat = []
for i in range(n):
    print("\nEnter Details :")
    pid = input("Enter Patient ID :")
    name = input("Enter Name of Patient :")
    age = int(input("Enter Age :"))
    disease = input("Enter Disease :")

    P = patient(pid,name,age,disease)
    Pat.append(P)

count = 0

print("\nDisplay Details")
for i in Pat:
    print(i.PatientID," ",i.Name," ",i.Age," ",i.Disease)


patient_id = input("\nEnter Patient ID :")
d = input("Enter Disease :")

for i in Pat:
    if i.PatientID==patient_id:
        print("\nPatient Found ")
        print(i.PatientID," ",i.Name," ",i.Age," ",i.Disease)

    if i.Disease == d:
        count = count + 1
    
print("\nPatient Above 60 ")
for  i in Pat:
    if i.Age > 60:
        print(i.PatientID," ",i.Name," ",i.Age," ",i.Disease)

print("\nPatients with Diabetes:",count)