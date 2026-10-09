# Assignment 47 - Exception Handing 
''' Question 4: 
BANK ACCOUNT MANAGEMENT SYSTEM

Scenario:
A bank wants to develop a simple Python-based application to manage customer
bank accounts.

The application must handle invalid transactions using custom exceptions.

Create a class named BankAccount with the following attributes:

1. account_number
2. account_holder
3. balance

Create the following custom exceptions:

1. InsufficientBalanceException
2. NegativeDepositException
3. InvalidWithdrawalException
4. InvalidAmountException

## Requirements:

Create the following methods:

1. deposit(amount)
2. withdraw(amount)
3. check_balance()
4. display_account_details()

## deposit(amount):

1. If the deposit amount is negative, raise:

   NegativeDepositException: Deposit amount cannot be negative

2. If the deposit amount is zero, raise:

   InvalidAmountException: Deposit amount must be greater than zero

3. Otherwise, add the amount to the account balance.

4. Display the updated balance.

## withdraw(amount):

1. If the withdrawal amount is negative, raise:

   InvalidWithdrawalException: Withdrawal amount cannot be negative

2. If the withdrawal amount is zero, raise:

   InvalidAmountException: Withdrawal amount must be greater than zero

3. If the withdrawal amount is greater than the available balance, raise:

   InsufficientBalanceException: Insufficient balance

4. Otherwise, deduct the amount from the balance.

5. Display the updated balance.

## MENU:

The program should be menu-driven.

Display the following menu repeatedly:

================================
BANK ACCOUNT SYSTEM
===================

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit

Enter your choice:

## Functional Requirements:

Option 1:
Ask the user for the deposit amount and perform the deposit operation.

Option 2:
Ask the user for the withdrawal amount and perform the withdrawal operation.

Option 3:
Display the current account balance.

Option 4:
Display:

Account Number:
Account Holder:
Available Balance:

Option 5:
Display:

Thank you for using Bank Account System

For invalid menu choices, display:

Invalid choice

## Exception Handling:

Every transaction must be handled using try-except.

The program should NOT terminate when an exception occurs.

After displaying the exception message, the menu should be displayed again.

## Sample Execution:

Enter Account Number:
ACC101

Enter Account Holder:
Rahul

Enter Initial Balance:
10000

================================
BANK ACCOUNT SYSTEM
===================

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit

Enter your choice:
1

Enter deposit amount:
5000

Deposit successful.
Available Balance: 15000

Enter your choice:
2

Enter withdrawal amount:
3000

Withdrawal successful.
Available Balance: 12000

Enter your choice:
2

Enter withdrawal amount:
20000

InsufficientBalanceException: Insufficient balance

Enter your choice:
1

Enter deposit amount:
-500

NegativeDepositException: Deposit amount cannot be negative

Enter your choice:
3

Available Balance: 12000

Enter your choice:
4

Account Number: ACC101
Account Holder: Rahul
Available Balance: 12000

Enter your choice:
5

Thank you for using Bank Account System
'''

class InsufficientBalanceException(Exception):
    pass


class NegativeDepositException(Exception):
    pass


class InvalidWithdrawalException(Exception):
    pass


class InvalidAmountException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositException(
                "Deposit amount cannot be negative"
            )

        if amount == 0:
            raise InvalidAmountException(
                "Deposit amount must be greater than zero"
            )

        self.balance += amount

        print("Deposit successful.")
        print("Available Balance:", self.balance)

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidWithdrawalException(
                "Withdrawal amount cannot be negative"
            )

        if amount == 0:
            raise InvalidAmountException(
                "Withdrawal amount must be greater than zero"
            )

        if amount > self.balance:
            raise InsufficientBalanceException(
                "Insufficient balance"
            )

        self.balance -= amount

        print("Withdrawal successful.")
        print("Available Balance:", self.balance)

    def check_balance(self):
        print("Available Balance:", self.balance)

    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Available Balance:", self.balance)


account_number = input("Enter Account Number:\n")
account_holder = input("Enter Account Holder:\n")
initial_balance = float(input("Enter Initial Balance:\n"))

account = BankAccount(
    account_number,
    account_holder,
    initial_balance
)


while True:
    print("BANK ACCOUNT SYSTEM")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = input("\nEnter your choice:\n")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount:\n"))
            account.deposit(amount)

        except NegativeDepositException as e:
            print("NegativeDepositException:", e)

        except InvalidAmountException as e:
            print("InvalidAmountException:", e)

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount:\n"))
            account.withdraw(amount)

        except InvalidWithdrawalException as e:
            print("InvalidWithdrawalException:", e)

        except InvalidAmountException as e:
            print("InvalidAmountException:", e)

        except InsufficientBalanceException as e:
            print("InsufficientBalanceException:", e)

    elif choice == "3":
        try:
            account.check_balance()

        except Exception as e:
            print(e)

    elif choice == "4":
        try:
            account.display_account_details()

        except Exception as e:
            print(e)

    elif choice == "5":
        print("Thank you for using Bank Account System")
        break

    else:
        print("Invalid choice")
