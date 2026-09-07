# Assignment 19
# Question 6 : Product Code Verification System

code1 = input("Enter the code 1 : ").lower()
code2 = input("Enter the code 2 : ").lower()

str1 = ""
str2 = ""

for ch1 in code1:
    if not(ch1.isspace()):
        str1= str1 + ch1

for ch2 in code2:
    if not(ch2.isspace()):
        str2 = str2 + ch2

# print(str1)
# print(str2)

if len(str1)== len(str2):
    c1 = 0
    c2 = 0
    matched = False
    
    for i in range(len(str1)):

        for j in range(len(str2)):
            if str1[i]==str2[j]:
                c1 = c1+1

        for j in range(len(str2)):
            if str1[i]==str2[j]:
                c2 = c2+1 

        if c1 == c2:
            matched = True
            break
    if matched:
        print ("Codes are matching")
    
    else:
        print("Not matched")


else:
    print("Not matched")        