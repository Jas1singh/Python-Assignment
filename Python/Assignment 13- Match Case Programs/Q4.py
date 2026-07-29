# Assignment 13
# Question 4 : Electricity Bill Management System

units = None
bill = 0
surcharge = 0

while True:
    print("\n1. Enter Units Consumed")
    print("2. Calculate Bill Amount")
    print("3. Apply Surcharge")
    print("4. Display Final Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            units = int(input("Enter units consumed: "))
            print("Units recorded successfully")

        case 2:
            if units is None:
                print("Please enter units consumed first")
            else:
                if units <= 100:
                    bill = units * 5
                elif units <= 200:
                    bill = 100 * 5 + (units - 100) * 7
                else:
                    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

                print("Bill Amount:", bill)

        case 3:
            if units is None:
                print("Please enter units consumed first")
            else:
                if bill == 0:
                    if units <= 100:
                        bill = units * 5
                    elif units <= 200:
                        bill = 100 * 5 + (units - 100) * 7
                    else:
                        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

                if bill > 2000:
                    surcharge = bill * 0.10
                else:
                    surcharge = bill * 0.05

                print("Surcharge:", surcharge)

        case 4:
            if units is None:
                print("Please enter units consumed first")
            else:
                total = bill + surcharge

                print("----- Final Bill -----")
                print("Units:", units)
                print("Bill Amount:", bill)
                print("Surcharge:", surcharge)
                print("Total Payable:", total)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

