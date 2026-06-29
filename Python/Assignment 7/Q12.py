# Assignment 7
# Question 12 : Multiplication of Digits

num = int(input("Enter number : "))

product = 1

while num > 0:
    digit = num % 10
    product = product * digit
    num = num // 10

print(product)

if product % 2 == 0:
    print("Obtained product is Even")
else:
    print("Obtained product is Odd")

