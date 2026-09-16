# Problem 20: Find the lowest frequency character.

s = input("Enter the String : ")

min = 9
minChar = ""
for i in s:
    c=0
    for j in s:
        if j == i:
            c+=1
    if c < min:
        min = c
        minChar = i    
         
print(minChar) 