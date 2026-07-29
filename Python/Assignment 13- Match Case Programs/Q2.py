# Assignment 13
# Question 2 : Employee Salary Processor

basic = None
hra = 0
da = 0
net = 0
tax = 0

while True:
    print("\n1. Enter Basic Salary")
    print("2. Calculate HRA and DA")
    print("3. Calculate Net Salary")
    print("4. Tax Deduction")
    print("5. Display Salary Slip")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            basic = float(input("Enter Basic Salary: "))
            print("Basic Salary recorded successfully")

        case 2:
            if basic is None:
                print("Please enter basic salary first")
            else:
                hra = basic * 0.20
                da = basic * 0.10
                print("HRA:", hra)
                print("DA:", da)

        case 3:
            if basic is None:
                print("Please enter basic salary first")
            else:
                net = basic + hra + da
                print("Net Salary (before tax):", net)

        case 4:
            if basic is None:
                print("Please enter basic salary first")
            else:
                if net == 0:
                    net = basic + hra + da

                if net > 50000:
                    tax = net * 0.10
                else:
                    tax = net * 0.05

                print("Tax Deduction:", tax)

        case 5:
            if basic is None:
                print("Please enter basic salary first")
            else:
                final = net - tax

                print("----- Salary Slip -----")
                print("Basic Salary:", basic)
                print("HRA:", hra)
                print("DA:", da)
                print("Net Salary:", net)
                print("Tax:", tax)
                print("Final Salary:", final)

        case 6:
            print("Exiting program... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

