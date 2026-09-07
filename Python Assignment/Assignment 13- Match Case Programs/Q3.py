# Assignment 13
# Question 3 : Smart Banking System

balance = None

while True:
    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            amount = float(input("Enter amount to deposit: "))
            if balance is None:
                balance = amount
            else:
                balance += amount
            print("Amount deposited successfully")

        case 2:
            if balance is None:
                print("No balance available. Please deposit first")
            else:
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= amount
                    print("Withdrawal successful")

        case 3:
            if balance is None:
                print("No balance available. Please deposit first")
            else:
                print("Current Balance:", balance)

        case 4:
            if balance is None:
                print("No balance available. Please deposit first")
            else:
                if balance > 50000:
                    interest = balance * 0.05
                else:
                    interest = balance * 0.03

                balance += interest
                print("Interest added:", interest)
                print("Updated Balance:", balance)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

