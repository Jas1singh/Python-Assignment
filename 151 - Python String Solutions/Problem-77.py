# Problem 77: Find the longest substring that appears at both ends.

s = input("Enter the String :")
count = 0
pairs = []
maxSub =""

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        pairs.append(sub)

max = len(pairs[0])
for i in pairs:
    if len(i)>max:
        maxSub = i
        max = len(i)
        if maxSub == s[:len(maxSub)] and maxSub == s[len(s)-len(maxSub):]:
            print(f'{maxSub}')
            break




