# Problem 73:  Find the longest palindromic substring.

s = input("Enter the String :")
count = 0
pairs = []
max = 0
maxSub =""

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        if sub==sub[::-1]:
            pairs.append(sub)

for i in pairs:
    if len(i)>max:
        maxSub = i
        max = len(i)

print(f'{maxSub}')

