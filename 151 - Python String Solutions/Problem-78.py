# Problem 78:  Find the longest mirror-image substring at both ends.

s = input("Enter the String :")

pairs = []
maxSub =""

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        pairs.append(sub)

max = 0
for i in pairs:
    if 2 * len(i) < len(s) and i == s[:len(i)] and i[::-1] == s[len(s)-len(i):]:
            if len(i)>max:
                 maxSub = i
                 max = len(i)

print(f'{maxSub}')
            
         

