# Problem 16:

s = input("Enter the String : ")
ch = input("Enter the character : ")

# print(s.count(ch))

c=0
for i in range(len(s)):
    if ch == s[i]:
        c+=1

print(c)        


