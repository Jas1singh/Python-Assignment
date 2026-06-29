# Assignment 10
# Question 1 : 

number = int(input("Enter the Number : "))
product = 1

while number>0:
    if number%2!=0:
        product = product * number

    number = number - 1    

print("Product = ",product)     