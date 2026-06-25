# Assignment 5
# Question 5 : An ATM system processes withdrawal requests.

Balance = int(input("Enter the balance : "))
withdrawal_Amount = int(input("Enter the withdrawal amount : "))


if Balance>=withdrawal_Amount:
    if withdrawal_Amount<=10000:
        pin = input("Enter the PIN : ")
        if pin.lower()=="correct":
            print("Transaction Successful")

        else:
            print("Invalid Pin")    
    
    else:
        print("Limit Exceeded")

else:
    print("Insufficient Balance")