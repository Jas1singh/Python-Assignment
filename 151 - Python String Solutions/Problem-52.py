# Problem 52: Remove all special characters. 

s = input("Enter String :")

for i in s:
    if i.isalnum():
        print(i,end="") 

    else:
        continue

