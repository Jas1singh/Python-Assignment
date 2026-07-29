# Assignment 11
# Question 10 : Zero Count Prime Scanner

n = int(input ())

zcount=0
sum = 0
lowest = 9

while n>0:
	digit = n % 10
	sum = sum + digit
	
	if digit < lowest:
		lowest = digit
		
	if digit==0:
		zcount+=1
	n = n // 10

total = sum + zcount 

final = total * lowest
	
print(zcount)
print (sum)
print(lowest)
print(final)

i=2

if final<=1:
	print("not prime")
	
else:
			while i<final:
				if final % i==0:
					print("not prime")
					break
				i=i+1
			
			else:
				print("prime ")




