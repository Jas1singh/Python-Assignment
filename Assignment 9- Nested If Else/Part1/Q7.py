# Assignment 9
# Question 7 : Smart Restaurant Order Processing System

order_amount = int(input("Enter the Order Amount : "))
cust_type = input("Enter the Customer Type : ").lower()
payment_method = input("Enter the Payment Method Type : ").lower()

if order_amount>=2000:
    if cust_type=="vip":
        if payment_method=="online":
            print("Offer = Free Dessert + 20% Discount")
        else:
            print("Offer = Free Dessert")    
    
    else:
        if order_amount>=5000:
            print("Offer = 15% Discount")
        else:
            print("Offer = 10% Discount")

else:
    if order_amount>=1000:
        if cust_type=="VIP":
            print("Offer = 10% Discount")

        else:
            print("Offer = 5% Discount") 

    else:
        print("No Offer")          