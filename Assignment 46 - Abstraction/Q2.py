# Assignment 46 - Abstraction 
''' Question 2: 
HOSPITAL PATIENT BILLING SYSTEM
============================================================

Develop a MENU-DRIVEN Hospital Patient Billing System.

The hospital treats different categories of patients:

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient

Every patient must perform common operations such as:

calculate_bill()
calculate_discount()
calculate_final_amount()
generate_bill()

However, the calculation rules are different for each type
of patient.

Therefore, use ABSTRACTION to design the system.

------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------

Create an abstract class:

Patient

It should contain appropriate abstract methods required for
billing.

Create the following child classes:

1. GeneralPatient
2. EmergencyPatient
3. InsurancePatient
4. CorporatePatient

------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit

Enter your choice:

------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------

Input:

Patient ID
Patient Name
Patient Age

Then display:

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient

Enter patient type:

------------------------------------------------------------
GENERAL PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.500
Room Charge       : Rs.1000 per day
Medicine Charge   : Actual amount
Discount          : No discount

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
EMERGENCY PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.1000
Emergency Charge : Rs.500
Room Charge       : Rs.2000 per day
Medicine Charge   : Actual amount
Discount          : No discount

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
INSURANCE PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.800
Room Charge       : Rs.1500 per day
Medicine Charge   : Actual amount

Insurance covers 70% of the total hospital bill.

Patient pays remaining 30%.

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
CORPORATE PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.700
Room Charge       : Rs.1200 per day
Medicine Charge   : Actual amount

Corporate Discount = 20%

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------

Enter Patient ID: P1025
Enter Patient Name: Rajesh
Enter Patient Age: 42

Select Patient Type:

1. General
2. Emergency
3. Insurance
4. Corporate

Enter choice: 3

Enter Number of Days: 4
Enter Medicine Charge: 3500

------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------

========================================
            PATIENT BILL
========================================

Patient ID       : P1025
Patient Name     : Rajesh
Patient Age      : 42
Patient Type     : Insurance

Consultation Fee : Rs.800.00
Room Charges     : Rs.6000.00
Medicine Charges : Rs.3500.00

----------------------------------------

Total Hospital Bill : Rs.10300.00

Insurance Coverage  : 70%
Insurance Amount    : Rs.7210.00

Patient Payable     : Rs.3090.00

Bill Status         : GENERATED

========================================

------------------------------------------------------------
OPTION 2: GENERATE PATIENT BILL
------------------------------------------------------------

Ask:

Enter Patient ID:

If patient exists, generate and display the bill according
to the patient's type.

The calculation must be performed by the appropriate child
class.

------------------------------------------------------------
OPTION 3: VIEW PATIENT BILL
------------------------------------------------------------

Ask:

Enter Patient ID:

Display the complete patient bill.

If patient does not exist:

Patient record not found.

------------------------------------------------------------
OPTION 4:
------------------------------------------------------------

Display:

Thank you for using Hospital Management System.
'''

from abc import ABC, abstractmethod

class Patient(ABC):

    def __init__(self, patient_id, patient_name, patient_age,
                 number_of_days, medicine_charge):

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.number_of_days = number_of_days
        self.medicine_charge = medicine_charge

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_final_amount(self):
        pass

    @abstractmethod
    def generate_bill(self):
        pass


class GeneralPatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 500
        self.room_charge = self.number_of_days * 1000

        self.total_bill = (
            self.consultation_fee
            + self.room_charge
            + self.medicine_charge
        )

        return self.total_bill

    def calculate_discount(self):

        self.discount = 0
        return self.discount

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount
        return self.final_amount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()


        print("\nPATIENT BILL\n")

        print("Patient ID       :", self.patient_id)
        print("Patient Name     :", self.patient_name)
        print("Patient Age      :", self.patient_age)
        print("Patient Type     : General")

        print("\nConsultation Fee : Rs.", f"{self.consultation_fee:.2f}")
        print("Room Charges     : Rs.", f"{self.room_charge:.2f}")
        print("Medicine Charges : Rs.", f"{self.medicine_charge:.2f}")
        print()

        print("Total Hospital Bill : Rs.",
              f"{self.total_bill:.2f}")

        print("Discount            : Rs.",
              f"{self.discount:.2f}")

        print("Patient Payable     : Rs.",
              f"{self.final_amount:.2f}")

        print("Bill Status         : GENERATED")
        print()



class EmergencyPatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 1000
        self.emergency_charge = 500
        self.room_charge = self.number_of_days * 2000

        self.total_bill = (
            self.consultation_fee
            + self.emergency_charge
            + self.room_charge
            + self.medicine_charge
        )

        return self.total_bill

    def calculate_discount(self):

        self.discount = 0
        return self.discount

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount
        return self.final_amount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

      
        print("\nPATIENT BILL\n")

        print("Patient ID       :", self.patient_id)
        print("Patient Name     :", self.patient_name)
        print("Patient Age      :", self.patient_age)
        print("Patient Type     : Emergency")

        print("\nConsultation Fee : Rs.", f"{self.consultation_fee:.2f}")
        print("Emergency Charge : Rs.", f"{self.emergency_charge:.2f}")
        print("Room Charges     : Rs.", f"{self.room_charge:.2f}")
        print("Medicine Charges : Rs.", f"{self.medicine_charge:.2f}")
        print()

        print("Total Hospital Bill : Rs.",
              f"{self.total_bill:.2f}")

        print("Discount            : Rs.",
              f"{self.discount:.2f}")

        print("Patient Payable     : Rs.",
              f"{self.final_amount:.2f}")

        print("Bill Status         : GENERATED")
        print()


class InsurancePatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 800
        self.room_charge = self.number_of_days * 1500

        self.total_bill = (
            self.consultation_fee
            + self.room_charge
            + self.medicine_charge
        )

        return self.total_bill

    def calculate_discount(self):

        self.insurance_percentage = 70

        self.insurance_amount = (
            self.total_bill * self.insurance_percentage / 100
        )

        return self.insurance_amount

    def calculate_final_amount(self):

        self.final_amount = (
            self.total_bill - self.insurance_amount
        )

        return self.final_amount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

       
        print("\nPATIENT BILL\n")

        print("Patient ID       :", self.patient_id)
        print("Patient Name     :", self.patient_name)
        print("Patient Age      :", self.patient_age)
        print("Patient Type     : Insurance")

        print("\nConsultation Fee : Rs.", f"{self.consultation_fee:.2f}")
        print("Room Charges     : Rs.", f"{self.room_charge:.2f}")
        print("Medicine Charges : Rs.", f"{self.medicine_charge:.2f}")
        print()

        print("Total Hospital Bill : Rs.",
              f"{self.total_bill:.2f}")

        print("\nInsurance Coverage  :",
              f"{self.insurance_percentage}%")

        print("Insurance Amount    : Rs.",
              f"{self.insurance_amount:.2f}")

        print("Patient Payable     : Rs.",
              f"{self.final_amount:.2f}")

        print("Bill Status         : GENERATED")

        print()


class CorporatePatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 700
        self.room_charge = self.number_of_days * 1200

        self.total_bill = (
            self.consultation_fee
            + self.room_charge
            + self.medicine_charge
        )

        return self.total_bill

    def calculate_discount(self):

        self.discount_percentage = 20

        self.discount = (
            self.total_bill * self.discount_percentage / 100
        )

        return self.discount

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount
        return self.final_amount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        print("\nPATIENT BILL\n")
        print("Patient ID       :", self.patient_id)
        print("Patient Name     :", self.patient_name)
        print("Patient Age      :", self.patient_age)
        print("Patient Type     : Corporate")

        print("\nConsultation Fee : Rs.", f"{self.consultation_fee:.2f}")
        print("Room Charges     : Rs.", f"{self.room_charge:.2f}")
        print("Medicine Charges : Rs.", f"{self.medicine_charge:.2f}")

        print()

        print("Total Hospital Bill : Rs.",
              f"{self.total_bill:.2f}")

        print("\nCorporate Discount  :",
              f"{self.discount_percentage}%")

        print("Discount Amount     : Rs.",
              f"{self.discount:.2f}")

        print("Patient Payable     : Rs.",
              f"{self.final_amount:.2f}")

        print("Bill Status         : GENERATED")

        print()


patient_records = {}


def register_patient():

    print("\nREGISTER PATIENT\n")

    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    patient_age = int(input("Enter Patient Age: "))

    print("\nSelect Patient Type:")
    print("1. General")
    print("2. Emergency")
    print("3. Insurance")
    print("4. Corporate")

    choice = input("Enter choice: ")

    number_of_days = int(input("Enter Number of Days: "))
    medicine_charge = float(input("Enter Medicine Charge: "))

    patient = None

    if choice == "1":

        patient = GeneralPatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )

    elif choice == "2":

        patient = EmergencyPatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )

    elif choice == "3":

        patient = InsurancePatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )

    elif choice == "4":

        patient = CorporatePatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )

    else:
        print("Invalid patient type.")
        return

    patient_records[patient_id] = patient

    print("\nPatient registered successfully.")


def generate_patient_bill():

    patient_id = input("\nEnter Patient ID: ")

    if patient_id not in patient_records:
        print("\nPatient record not found.")
        return

    patient = patient_records[patient_id]

    patient.generate_bill()


def view_patient_bill():

    patient_id = input("\nEnter Patient ID: ")

    if patient_id not in patient_records:
        print("\nPatient record not found.")
        return

    patient = patient_records[patient_id]

    patient.generate_bill()



while True:

    print("\n========================================")
    print("       HOSPITAL MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Register Patient")
    print("2. Generate Patient Bill")
    print("3. View Patient Bill")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        register_patient()

    elif choice == "2":

        generate_patient_bill()

    elif choice == "3":

        view_patient_bill()

    elif choice == "4":

        print("\nThank you for using Hospital Management System.")
        break

    else:

        print("\nInvalid choice. Please try again.")