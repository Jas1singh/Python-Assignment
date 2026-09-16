# Assignment 5
# Question 3 : E-Commerce Offer Engine

value = int(input("Enter the cart value : "))

if value>=500:
    print("\nFree Delivery")
    if value>=1000:
        print("Discount coupon unlocked")

else:
    print("Free delivery not available")
