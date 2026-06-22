# Assignment 4
# Question 2 : Mobile EMI Calculation

Mobile_price = int(input("Enter the total mobile price : "))
Down_Payment = int(input("Enter the down payment amount : "))
interest_Rate = int (input("Enter the interest rate : "))
Total_Months = int (input("Enter the installment months : "))

Mobile_price = Mobile_price-Down_Payment
Total_With_Interest = (Mobile_price*10/100)+Mobile_price

EMI = Total_With_Interest/Total_Months

print("Remaining Amount = ", Mobile_price)
print("Total with Interest = ", Total_With_Interest)
print("Monthly EMI = ", EMI)
