# Problem 79: Divide a string into n equal parts.

s = input("Enter the String :")

n = int(input("No. of parts of string :"))

part = len(s)//n

for i in range(0,len(s),part):
        print(s[i:i+part])

