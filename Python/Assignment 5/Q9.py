# Assignment 5
# Question 9 : Library Access System

membership = input("Membership Active (yes/no) : ")

if membership.lower()=="yes":
    books =int(input("How many books are issued ? : "))
    print("Entry allowed")
    if books<3:
        print("Can issue more books")

else:
    print("Not allowed")

