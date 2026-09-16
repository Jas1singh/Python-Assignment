# Problem 61: Count total alphabets, digits, and special characters. 

s = input("Enter the String :")

c1 = 0
c2 = 0
c3 = 0

for i in s:
    if i.isalpha():
        c1+=1

    elif i.isdigit():
        c2+=1

    else:
        c3+=1 

print("Alphabets :",c1)               
print("Digits :",c2)               
print("Special :",c3)               


