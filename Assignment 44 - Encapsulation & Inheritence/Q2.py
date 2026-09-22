# Assignment 44 - Encapsulation & Inheritence 
''' Question 2: 
BANK ACCOUNT MANAGEMENT SYSTEM
=============================================

A bank provides different types of accounts.

Create the following hierarchy:

Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount

REQUIREMENTS:

1. Create a parent class Account.

Attributes:

* account_number
* customer_name
* balance

2. SavingsAccount should inherit from Account.

Additional attribute:

* interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.

Additional attribute:

* cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:

display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:

@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.

INPUT:

Enter Account Number:
Enter Customer Name:
Enter Initial Balance:
Enter Account Type:

1. Savings Account
2. Premium Savings Account

For Savings Account:

Enter Interest Rate:

For Premium Savings Account:

Enter Interest Rate:
Enter Cashback Percentage:

Then ask:

Enter amount to deposit:
Enter amount to withdraw:

SAMPLE INPUT:

Enter Account Number: 1001
Enter Customer Name: Amit
Enter Initial Balance: 25000
Enter Account Type: 2
Enter Interest Rate: 7
Enter Cashback Percentage: 2
Enter amount to deposit: 5000
Enter amount to withdraw: 3000

EXPECTED OUTPUT:

## Account Details

Account Number: 1001
Customer Name: Amit
Balance: 25000

Account Type: Premium Savings Account
Interest Rate: 7%
Cashback Percentage: 2%

After Deposit:
Balance: 30000

After Withdrawal:
Balance: 27000

'''

class Account:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance


    @property
    def balance(self):
        return self._balance


    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative.")
            self._balance = 0
        else:
            self._balance = value

   
    @balance.deleter
    def balance(self):
        del self._balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance - amount

    def display_account(self):
        print("## Account Details")
        print()
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def display_account(self):
        super().display_account()
        print()
        print("Account Type: Savings Account")
        print(f"Interest Rate: {self.interest_rate}%")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(
        self,
        account_number,
        customer_name,
        balance,
        interest_rate,
        cashback_percentage
    ):
        super().__init__(
            account_number,
            customer_name,
            balance,
            interest_rate
        )
        self.cashback_percentage = cashback_percentage

    def display_account(self):
        super().display_account()
        print(f"Cashback Percentage: {self.cashback_percentage}%")


# Taking input from user

account_number = int(input("Enter Account Number: "))
customer_name = input("Enter Customer Name: ")
initial_balance = float(input("Enter Initial Balance: "))

print("Enter Account Type:")
print("1. Savings Account")
print("2. Premium Savings Account")

account_type = int(input("Enter Account Type: "))

if account_type == 1:

    interest_rate = float(input("Enter Interest Rate: "))

    account = SavingsAccount(
        account_number,
        customer_name,
        initial_balance,
        interest_rate
    )

elif account_type == 2:

    interest_rate = float(input("Enter Interest Rate: "))
    cashback_percentage = float(input("Enter Cashback Percentage: "))

    account = PremiumSavingsAccount(
        account_number,
        customer_name,
        initial_balance,
        interest_rate,
        cashback_percentage
    )

else:
    print("Invalid Account Type.")
    exit()


print()
account.display_account()


deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

print()
print("After Deposit:")
print(f"Balance: {account.balance}")


withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

print()
print("After Withdrawal:")
print(f"Balance: {account.balance}")
