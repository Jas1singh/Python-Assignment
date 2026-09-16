# Assignment 20
# Question 7 : Advanced Smart Chat Compression Expansion System

msg = input("Enter the Compressed message :")

result = ""

for i in range(len(msg)):
    if msg[i].isalpha():
        ch = msg[i].lower()
        i = i+1

        num = ""
        while i < len(msg) and msg[i].isdigit():
            num = num + msg[i]
            i = i+1

        if num !="":
            result = result + ch * int(num)        

    else:
        i = i+1

print(result)        
print(len(result))        