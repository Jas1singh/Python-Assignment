# Problem 57:  Merge two strings alternatively.

s1 = input("Enter the S1 :")
s2 = input("Enter the S2 :")

n = min(len(s1), len(s2))

result = ""
for i in range(n):
    result = result + s1[i]
    result = result + s2[i]  

result += s1[n:]
result += s2[n:]

print(result)               


