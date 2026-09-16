# Assignment 5
# Question 7 : dayType = input("What is the Day Type  (weekday/weekend) : ")


Experience = int(input("Enter your experience (in years) : "))

if Experience>=5:
    rating = int(input("Enter the rating : "))
    salary = int(input("Enter your salary : "))
    if rating>=4:
        if salary<50000:
            Bonus = salary * 0.20
            print("Bonus = ", Bonus)

        else:
            Bonus = salary * 0.10
            print("Bonus = ", Bonus)  

    else:
        Bonus = salary * 0.05
        print("Bonus = ", Bonus)   

else:
    print("No bonus given")                 


