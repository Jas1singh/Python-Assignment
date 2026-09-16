# Assignment 12
# Question 5 : Number Stability Analyzer

n  = int(input ())

high = 9
# temp = n
# while temp > 0:
#     digits += 1
#     temp //= 10

count = len(str(n))

for i in range(count-1):
    digit = n % 10
    n = n // 10
        
    if n%10>digit:
        print("Unstable Number")
        break

else:
	print ("Stable Number")

