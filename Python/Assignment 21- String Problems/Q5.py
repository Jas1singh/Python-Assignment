# Assignment 21
''' Question 5 : Find the Number of Unique Characters in a String
                 Password Strength Analyzer '''

password = input("Enter the password :")

unique =""

for ch in password:
    if ch not in unique:
        unique = unique + ch

length = len(unique)

print(length)



