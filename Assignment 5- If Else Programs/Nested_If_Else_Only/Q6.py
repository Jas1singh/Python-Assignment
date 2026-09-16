# Assignment 5
# Question 6 : A movie theatre calculates ticket prices based on age, show time, and day type.


age = int(input("Enter your age : "))
showTime = input("Enter The Show Time (morning/evening) : ")

if age<18:
    
    if showTime.lower()=="morning":
        print("Ticket Price = 100")

    else:
        print("Ticket Price = 150")

else:
    if showTime.lower()=="evening":
         dayType = input("What is the Day Type  (weekday/weekend) : ")
         if dayType.lower()=="weekend":
            print("Ticket Price = 300")

         else:
             print("Ticket Price = 250")
    
    else:
        print("Ticket Price = 200")

                



        
