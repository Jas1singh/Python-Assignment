# Problem 50: Remove all digits.

s = input("Enter String :")

for i in s:
    if i.isdigit():
        continue
    else:
        print(i,end="") 