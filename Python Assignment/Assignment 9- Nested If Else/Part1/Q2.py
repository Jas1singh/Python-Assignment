# Assignment 9
# Question 2 : Smart Warehouse Dispatch System

stock_available = int(input("Enter the stock availability : "))
Priority_level = (input("Enter the Priority level  : "))
delivery_distance = int(input("Enter the delivery Distance : "))

if stock_available>=100:
    if Priority_level.lower()=="high":
        if delivery_distance<=200:
            print("Dispatch Status = Dispatch Immediately")
        else:
            print("Dispatch Status = Dispatch via Fast Courier")
    else:
        if stock_available>=300:
            print("Dispatch Status = Bulk Dispatch")

elif stock_available<100:
    if stock_available>=50:
        if Priority_level.lower()=="high":
            print("Dispatch Status = Partially Dispatch")

        else:
            print("Hold")

    else:
        print("Out Of Stock")                               