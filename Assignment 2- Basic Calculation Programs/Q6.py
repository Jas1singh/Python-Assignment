# Python Assignment 2
# Question 6 : Smart Coin Machine

amount = int(input("Enter amount: ₹"))

ten_rupee_coins = amount // 10
remaining = amount % 10

five_rupee_coins = remaining // 5

print("₹10 x", ten_rupee_coins, ", ₹5 x", five_rupee_coins)