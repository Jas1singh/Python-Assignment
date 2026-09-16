# Assignment 16
# Question 10 : Electricity Bill Processing System (Multi-House)

n = int (input("Enter the Number Of Houses : "))

total_collection = 0
highest_bill = 0

for i in range(1,n+1):
    units = int(input(f"Enter the No. of Units for House {i} :"))


    if units>0 and units<=100:
        bill = units * 5

    elif units>100 and units<=200:
        bill = (units - 100)*7 + 100 * 5

    else:
        bill = (units-200)*10 + 100 *7 + 100 * 5


    if bill > 2000:
        bill += bill * 0.10

    if units < 50:
        bill -= 100

    print(f"House {i} Bill = {int(bill)}")

    total_collection += bill

    if bill > highest_bill:
        highest_bill = bill

print()
print("Total Collection =", int(total_collection))
print("Highest Bill =", int(highest_bill))







