# Assignment 3
# Question 13 : Compound Interest Calculator

principal = int(input("Enter principal amt: "))
rate = float(input("Enter rate (%): "))
time = float(input("Enter time (years): "))

amount = principal * ((1 + rate / 100) ** time)
compoundInterest = amount - principal

print("Amount =", amount)
print("Compound Interest =", compoundInterest)

