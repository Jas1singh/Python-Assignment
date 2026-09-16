# Assignment 5
# Question 4 : A gym provides personalized plans based on age, weight, and fitness goal.


age = int(input("Enter your age : "))

if age>=18:
    weight = int(input("Enter your weight : "))
    if weight>=80:
        goal = (input("Enter your goal (weight loss or muscle gain) : "))
        if goal.lower()=="weight loss":
            print("Plan = Cardio Plan")

        else:
            print("Plan = Strength Plan")

    else:
        print("Plan = General Fitness Plan") 

else:
    print("Not Allowed")

