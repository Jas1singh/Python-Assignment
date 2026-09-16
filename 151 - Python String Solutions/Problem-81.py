# Problem 81:  Generate a hash code or UUID.

s = input("Enter the string : ")
n = len(s)
hash = 0

for i in range(n):
    hash = hash + ord(s[i])*(31**(n-i-1))

print(hash)




