from Assignment4.Bank_Account_System import class_module

accounts = []

for i in range(5):
    print(f"\nEnter details of Account {i + 1}")

    account_no = int(input("Enter Account No: "))
    customer_name = input("Enter Customer Name: ")
    balance = float(input("Enter Balance: "))

    account = class_module.Account(
        account_no,
        customer_name,
        balance
    )

    accounts.append(account)


print("\nAll Accounts:")
for account in accounts:
    account.display()


search_account_no = int(input("\nEnter Account No for deposit: "))

selected_account = None

for account in accounts:
    if account.account_no == search_account_no:
        selected_account = account
        break

if selected_account:
    amount = float(input("Enter amount to deposit: "))
    selected_account.deposit(amount)

    print("\nAfter Deposit:")
    selected_account.display()
else:
    print("\nAccount Not Found")


search_account_no = int(input("\nEnter Account No for withdrawal: "))

selected_account = None

for account in accounts:
    if account.account_no == search_account_no:
        selected_account = account
        break

if selected_account:
    amount = float(input("Enter amount to withdraw: "))

    if selected_account.withdraw(amount):
        print("\nAfter Withdrawal:")
        selected_account.display()
    else:
        print("\nInsufficient Balance")
else:
    print("\nAccount Not Found")


print("\nAccounts having balance greater than 50000:")

for account in accounts:
    if account.balance > 50000:
        account.display()

highest_balance_account = max(
    accounts,
    key=lambda account: account.balance
)

print("\nHighest Balance Account:")
highest_balance_account.display()
