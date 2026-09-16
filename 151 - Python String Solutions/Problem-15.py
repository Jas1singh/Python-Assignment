# Problem 15:

s = input("Enter the String : ")
ch = input("Enter the character : ")

for i in range(len(s)-1,-1,-1):
    if ch == s[i]:
        print(i)
        break
