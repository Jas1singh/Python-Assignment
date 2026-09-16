# Problem 53: Remove punctuation.

s = input("Enter String :")
special ="@#$%^&*"

for i in s:
    if i.isalnum() or i.isspace() or i in special:
        print(i,end="")
        
    else:
        continue

