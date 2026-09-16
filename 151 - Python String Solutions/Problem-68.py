# Problem 68:  Count the sum of digits present in a string. 

s = input("Enter the String :")

sum = 0 
for i in s:
    if i.isdigit():
        sum = sum + int(i)

print(sum)


