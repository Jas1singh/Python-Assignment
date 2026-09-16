# Problem 55: Reverse only vowels.

s = input("Enter String :")

vowels ="aeiouAEIOU"
rev = ""

for i in s:
    if i in vowels:
        rev = i + rev

result = ""
j = 0
for i in s:
    if i in vowels:
        result = result + rev[j]
        j = j+1

    else:
        result = result + i     

print(result)        

