# Problem 14:

s = input("Enter the String : ")
ch = input("Enter the character : ")

# print(s.index(ch))

for i in range(len(s)):
    if ch == s[i]:
        print(i)
        break
