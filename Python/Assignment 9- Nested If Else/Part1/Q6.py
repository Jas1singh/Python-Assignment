# Assignment 9
# Question 6 : Multi-Level Employee Promotion System


experience = int(input("Enter the Experience : "))
rating = int(input("Enter the rating : "))
projects = int(input("Enter the projected completed : "))

if experience>=5:
    if rating>=4:
        if projects>=3:
            salary = int(input("Enter the Salary : "))
            if salary<=50000:
                print("Promotion Status = Promoted with 30% hike")
            else:
                print("Promotion Status = Promoted with 20% hike")
        else:
            print("Promotion Status = Promoted with 10% hike")    
    
    else:
        print("No Promotion")

else:
    if rating==5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("No Promotion")          