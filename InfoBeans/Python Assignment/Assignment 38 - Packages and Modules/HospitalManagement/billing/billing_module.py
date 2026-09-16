''' 
Billing Package

Create a package named "billing".

Create module:
billing_module.py


Implement:


generate_bill()


Take:

- Patient ID
- Consultation Charges
- Medicine Cost
- Test Charges


Calculate total amount:

Total Bill = Consultation Charges + Medicine Cost + Test Charges


Display complete bill.

'''

def generate_bill(patient_id, consultation_charges, medicine_cost, test_charges):
    total_bill = consultation_charges + medicine_cost + test_charges

    print("\n                  Bill Details ")
    print("Patient ID : ",patient_id)
    print("Consultation Charges : ",consultation_charges)
    print("Medicine Cost : ",medicine_cost)
    print("Test Charges : ",test_charges)
    print()

    print("Total Bill : ",total_bill)



