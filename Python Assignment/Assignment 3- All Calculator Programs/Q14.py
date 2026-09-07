# Assignment 3
# Question 14 :  Simple Profit or Loss Calculator

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

ProfitOrLoss = sp-cp
 
ProfitOrLossPer = (ProfitOrLoss/cp) *100

print("Profit or Loss =", ProfitOrLoss)
print("Profit or Loss Percentage =", ProfitOrLossPer)

