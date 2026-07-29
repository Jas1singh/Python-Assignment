# Assignment 5
# Question 2 : An e-commerce website provides discounts based on the cart value and user type.

cartValue = int(input("Enter the cart value : "))

if cartValue>=5000:
    user = (input("Enter the user type (premium or regular) : "))
    if user.lower()=="premium":
        final = cartValue - (cartValue * 0.20)
        print("Final Amount = ", final)

    else:
        final = cartValue - (cartValue * 0.10)
        print("Final Amount = ", final)

else:
    if cartValue>=2000:
        final = cartValue - (cartValue * 0.05)
        print("Final Amount = ", final)

    else:
        print("No Discount for You")    








