# Problem 51: Extract only digits. 

s = input("Enter String :")

for i in s:
    if i.isdigit():
        print(i,end="")
        
    else:
        continue

