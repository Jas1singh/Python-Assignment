# Assignment 46 - Abstraction 
''' Question 1: 
ONLINE PAYMENT MANAGEMENT SYSTEM
============================================================

Develop a MENU-DRIVEN Online Payment Management System for an
e-commerce company.

The company supports different payment methods:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Every payment method follows a common payment process, but the
actual validation, authentication, processing fee and payment
processing logic are different.

Therefore, the system must be designed using ABSTRACTION.

------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------

Create an abstract class named:

Payment

The class should define the following abstract methods:

1. validate_payment()
2. calculate_processing_fee()
3. authenticate_payment()
4. process_payment()
5. generate_receipt()

Create separate child classes for:

1. UPIPayment
2. CreditCardPayment
3. DebitCardPayment
4. NetBankingPayment
5. WalletPayment

Each child class must provide its own implementation of all
required abstract methods.

------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit

Enter your choice:

------------------------------------------------------------
OPTION 1: MAKE PAYMENT
------------------------------------------------------------

Ask the user to enter:

Customer Name
Order ID
Order Amount

Then display:

Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Enter your choice:

------------------------------------------------------------
UPI:
------------------------------------------------------------

Input:

UPI ID
UPI PIN

Processing Fee:

0%

------------------------------------------------------------
CREDIT CARD:
------------------------------------------------------------

Input:

Card Number
Card Holder Name
CVV
Expiry Date

Processing Fee:

2% of Order Amount

------------------------------------------------------------
DEBIT CARD:
------------------------------------------------------------

Input:

Card Number
Card Holder Name
CVV
Expiry Date

Processing Fee:

1% of Order Amount

------------------------------------------------------------
NET BANKING:
------------------------------------------------------------

Input:

Bank Name
Account Number
Customer ID

Processing Fee:

0.5% of Order Amount

------------------------------------------------------------
WALLET:
------------------------------------------------------------

Input:

Wallet Name
Mobile Number
Wallet PIN

Processing Fee:

1.5% of Order Amount

------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------

Enter Customer Name: Rahul
Enter Order ID: ORD1052
Enter Order Amount: 5000

Select Payment Method:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Enter your choice: 2

Enter Card Number: 4567891234567890
Enter Card Holder Name: Rahul Singh
Enter CVV: 321
Enter Expiry Date: 12/29

------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------

========================================
          PAYMENT PROCESSING
========================================

Customer Name       : Rahul
Order ID            : ORD1052
Payment Method      : Credit Card

Order Amount        : Rs.5000.00
Processing Fee      : Rs.100.00
Final Amount        : Rs.5100.00

Validating payment details...
Payment details validated successfully.

Authenticating payment...
Authentication successful.

Processing payment...
Payment processed successfully.

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================

OPTION 2: VIEW PAYMENT DETAILS
------------------------------------------------------------

Ask:

Enter Order ID:

If the order exists, display:

Order ID
Customer Name
Payment Method
Order Amount
Processing Fee
Final Amount
Transaction ID
Payment Status

If the order does not exist:

Payment record not found.

OPTION 3:

Display:

Thank you for using Online Payment System.
'''


from abc import ABC, abstractmethod
import random

class Payment(ABC):

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def calculate_processing_fee(self):
        pass

    @abstractmethod
    def authenticate_payment(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass

class UPIPayment(Payment):

    def __init__(self, upi_id, upi_pin, amount):
        self.upi_id = upi_id
        self.upi_pin = upi_pin
        self.amount = amount
        self.fee = 0

    def validate_payment(self):
        if "@" in self.upi_id and len(self.upi_pin) == 4:
            print("Payment details validated successfully.")
            return True

        print("Invalid UPI details.")
        return False

    def calculate_processing_fee(self):
        self.fee = 0
        return self.fee

    def authenticate_payment(self):
        if len(self.upi_pin) == 4:
            print("Authentication successful.")
            return True

        print("Authentication failed.")
        return False

    def process_payment(self):
        print("Payment processed successfully.")
        return True

    def generate_receipt(self):
        return self.fee


class CreditCardPayment(Payment):

    def __init__(self, card_number, card_holder, cvv, expiry_date, amount):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.amount = amount
        self.fee = 0

    def validate_payment(self):
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            print("Payment details validated successfully.")
            return True

        print("Invalid Credit Card details.")
        return False

    def calculate_processing_fee(self):
        self.fee = self.amount * 0.02
        return self.fee

    def authenticate_payment(self):
        if len(self.cvv) == 3:
            print("Authentication successful.")
            return True

        print("Authentication failed.")
        return False

    def process_payment(self):
        print("Payment processed successfully.")
        return True

    def generate_receipt(self):
        return self.fee


class DebitCardPayment(Payment):

    def __init__(self, card_number, card_holder, cvv, expiry_date, amount):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.amount = amount
        self.fee = 0

    def validate_payment(self):
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            print("Payment details validated successfully.")
            return True

        print("Invalid Debit Card details.")
        return False

    def calculate_processing_fee(self):
        self.fee = self.amount * 0.01
        return self.fee

    def authenticate_payment(self):
        if len(self.cvv) == 3:
            print("Authentication successful.")
            return True

        print("Authentication failed.")
        return False

    def process_payment(self):
        print("Payment processed successfully.")
        return True

    def generate_receipt(self):
        return self.fee


class NetBankingPayment(Payment):

    def __init__(self, bank_name, account_number, customer_id, amount):
        self.bank_name = bank_name
        self.account_number = account_number
        self.customer_id = customer_id
        self.amount = amount
        self.fee = 0

    def validate_payment(self):
        if len(self.account_number) >= 8 and self.customer_id != "":
            print("Payment details validated successfully.")
            return True

        print("Invalid Net Banking details.")
        return False

    def calculate_processing_fee(self):
        self.fee = self.amount * 0.005
        return self.fee

    def authenticate_payment(self):
        if self.customer_id != "":
            print("Authentication successful.")
            return True

        print("Authentication failed.")
        return False

    def process_payment(self):
        print("Payment processed successfully.")
        return True

    def generate_receipt(self):
        return self.fee


class WalletPayment(Payment):

    def __init__(self, wallet_name, mobile_number, wallet_pin, amount):
        self.wallet_name = wallet_name
        self.mobile_number = mobile_number
        self.wallet_pin = wallet_pin
        self.amount = amount
        self.fee = 0

    def validate_payment(self):
        if len(self.mobile_number) == 10 and len(self.wallet_pin) == 4:
            print("Payment details validated successfully.")
            return True

        print("Invalid Wallet details.")
        return False

    def calculate_processing_fee(self):
        self.fee = self.amount * 0.015
        return self.fee

    def authenticate_payment(self):
        if len(self.wallet_pin) == 4:
            print("Authentication successful.")
            return True

        print("Authentication failed.")
        return False

    def process_payment(self):
        print("Payment processed successfully.")
        return True

    def generate_receipt(self):
        return self.fee


payment_records = {}

def make_payment():

    print("\nMAKE PAYMENT\n")

    customer_name = input("Enter Customer Name: ")
    order_id = input("Enter Order ID: ")
    amount = float(input("Enter Order Amount: "))

    print("\nSelect Payment Method:")
    print("1. UPI")
    print("2. Credit Card")
    print("3. Debit Card")
    print("4. Net Banking")
    print("5. Wallet")

    choice = input("Enter your choice: ")

    payment = None
    payment_method = ""

    if choice == "1":

        upi_id = input("Enter UPI ID: ")
        upi_pin = input("Enter UPI PIN: ")

        payment = UPIPayment(upi_id, upi_pin, amount)
        payment_method = "UPI"

    elif choice == "2":

        card_number = input("Enter Card Number: ")
        card_holder = input("Enter Card Holder Name: ")
        cvv = input("Enter CVV: ")
        expiry_date = input("Enter Expiry Date: ")

        payment = CreditCardPayment(
            card_number,
            card_holder,
            cvv,
            expiry_date,
            amount
        )

        payment_method = "Credit Card"

    elif choice == "3":

        card_number = input("Enter Card Number: ")
        card_holder = input("Enter Card Holder Name: ")
        cvv = input("Enter CVV: ")
        expiry_date = input("Enter Expiry Date: ")

        payment = DebitCardPayment(
            card_number,
            card_holder,
            cvv,
            expiry_date,
            amount
        )

        payment_method = "Debit Card"

    elif choice == "4":

        bank_name = input("Enter Bank Name: ")
        account_number = input("Enter Account Number: ")
        customer_id = input("Enter Customer ID: ")

        payment = NetBankingPayment(
            bank_name,
            account_number,
            customer_id,
            amount
        )

        payment_method = "Net Banking"

    elif choice == "5":

        wallet_name = input("Enter Wallet Name: ")
        mobile_number = input("Enter Mobile Number: ")
        wallet_pin = input("Enter Wallet PIN: ")

        payment = WalletPayment(
            wallet_name,
            mobile_number,
            wallet_pin,
            amount
        )

        payment_method = "Wallet"

    else:
        print("Invalid payment method.")
        return

    fee = payment.calculate_processing_fee()

    print("\nPAYMENT PROCESSING\n")
    print("Customer Name       :", customer_name)
    print("Order ID            :", order_id)
    print("Payment Method      :", payment_method)

    print(f"\nOrder Amount        : Rs.{amount:.2f}")
    print(f"Processing Fee      : Rs.{fee:.2f}")
    print(f"Final Amount        : Rs.{amount + fee:.2f}")

    print("\nValidating payment details...")

    if not payment.validate_payment():
        print("Payment failed.")
        return

    print("\nAuthenticating payment...")

    if not payment.authenticate_payment():
        print("Payment failed.")
        return

    print("\nProcessing payment...")

    if not payment.process_payment():
        print("Payment failed.")
        return

    transaction_id = "TXN" + str(random.randint(100000, 999999))

    payment_records[order_id] = {
        "customer_name": customer_name,
        "order_id": order_id,
        "payment_method": payment_method,
        "order_amount": amount,
        "processing_fee": fee,
        "final_amount": amount + fee,
        "transaction_id": transaction_id,
        "payment_status": "SUCCESS"
    }

    print("\nTransaction ID      :", transaction_id)
    print("Payment Status      : SUCCESS")
    print()


def view_payment_details():

    order_id = input("\nEnter Order ID: ")

    if order_id not in payment_records:
        print("\nPayment record not found.")
        return

    record = payment_records[order_id]

    
    print("\nPAYMENT DETAILS\n")
    print("Order ID            :", record["order_id"])
    print("Customer Name       :", record["customer_name"])
    print("Payment Method      :", record["payment_method"])
    print(f"Order Amount        : {record['order_amount']:.2f}")
    print(f"Processing Fee      : {record['processing_fee']:.2f}")
    print(f"Final Amount        : {record['final_amount']:.2f}")
    print("Transaction ID      :", record["transaction_id"])
    print("Payment Status      :", record["payment_status"])

    print()


while True:

    print("\n========================================")
    print("       ONLINE PAYMENT SYSTEM")
    print("========================================")

    print("1. Make Payment")
    print("2. View Payment Details")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        make_payment()

    elif choice == "2":
        view_payment_details()

    elif choice == "3":
        print("\nThank you for using Online Payment System.")
        break

    else:
        print("\nInvalid choice. Please try again.")