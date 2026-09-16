# Problem 19: Find the highest frequency character.

s = input("Enter the String : ")

max = 0
maxChar = ""
for i in s:
    c=0
    for j in s:
        if j == i:
            c+=1
    if c > max:
        max = c
        maxChar = i    
         
print(maxChar)        
        