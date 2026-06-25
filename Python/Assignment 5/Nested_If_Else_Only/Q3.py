# Assignment 5
# Question 3 : A smart electricity monitoring system categorizes us
# age levels for better energy management.

units = int(input("Enter the no. of units : "))

if units>=100:
    if units>=300:
        print("Usage Category = High Usage")

    else:
        if units>=200:
            print("Usage Category = Moderate Usage")

        else:
            print("Usage Category = Normal Usage")

else:
    print("Usage Category = Low usage")                    


    