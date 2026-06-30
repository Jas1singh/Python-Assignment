# Assignment 12
# Question 4 : Unique Digit Security Scanner

n  = int(input ())

# temp = n
# while temp > 0:
#     digits += 1
#     temp //= 10

count = len(str(n))

for i in range(count-1):
    digit = n % 10
    n = n // 10
        
    if n%10==digit:
        print("Invalid Code")
        break

else:
	print ("Valid Unique Code")