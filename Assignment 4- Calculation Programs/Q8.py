# Assignment 4
# Question 8 : Compound Interest

principal = int(input("Enter principal amt: "))
rate = float(input("Enter rate (%): "))
time = float(input("Enter time (years): "))

Compound_Interest = principal * ((1 + rate / 100) ** time)

print("Amount after interest =", Compound_Interest)