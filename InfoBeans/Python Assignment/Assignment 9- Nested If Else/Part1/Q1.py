# Assignment 9
# Question 1 : E-Learning Course Access System

Sub_type = input("Enter the Subscription Type : ")
cProgress = int(input("Enter the course progress : "))
testScore = int(input("Enter the test Score : "))

if Sub_type.lower()=="premium":
    if cProgress>=80:
        if testScore>=70:
            print("Unlock Certificate")
        else:
            print("Access Status = Retry Test")
    else:
        print("Access Status = Complete Course")

elif Sub_type.lower()=="basic":
    if cProgress>=50:
        print("Access Status = Limited Access")
    else:
        print("Content is locked")

else:
    print("Access Status = Deny Access")


