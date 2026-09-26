# Assignment 45 -Polymorphism 
''' Question 3: 
Bank Account System

Create a parent class BankAccount with:

account_no
holder_name
balance

Create two child classes:

SavingsAccount
CurrentAccount
Requirements
Take account details from the user.
Use super() to initialize the common attributes.
Create a method calculate_interest() in the parent class.
Override this method in both child classes.
Savings Account gets 5% interest.
Current Account gets 2% interest.
Display the account details and calculated interest.
Sample Input
Enter Account Number: 1001
Enter Holder Name: Amit
Enter Balance: 50000
Enter Account Type: Savings


Expected Output
----- Account Details -----
Account Number : 1001
Holder Name    : Amit
Balance        : 50000
Account Type   : Savings
Interest Rate  : 5%
Interest       : 2500
Amount After Interest : 52500

'''

class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def calculate_interest(self):
        return 0


class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance):
        super().__init__(account_no, holder_name, balance)

    def calculate_interest(self):
        return self.balance * 0.05


class CurrentAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance):
        super().__init__(account_no, holder_name, balance)

    def calculate_interest(self):
        return self.balance * 0.02


account_no = input("Enter Account Number: ")
holder_name = input("Enter Holder Name: ")
balance = float(input("Enter Balance: "))
account_type = input("Enter Account Type: ")


if account_type.lower() == "savings":
    account = SavingsAccount(account_no, holder_name, balance)
    interest_rate = "5%"
elif account_type.lower() == "current":
    account = CurrentAccount(account_no, holder_name, balance)
    interest_rate = "2%"
else:
    print("Invalid Account Type")
    exit()


interest = account.calculate_interest()
amount_after_interest = balance + interest


print("\n----- Account Details -----")
print("Account Number :", account.account_no)
print("Holder Name    :", account.holder_name)
print("Balance        :", int(account.balance))
print("Account Type   :", account_type)
print("Interest Rate  :", interest_rate)
print("Interest       :", int(interest))
print("Amount After Interest :", int(amount_after_interest))
