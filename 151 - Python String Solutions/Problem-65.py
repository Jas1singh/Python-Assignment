# Problem 65:  Count palindromic substrings.

s = input("Enter the String :")
count = 0
pairs = []

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        temp = sub
        pairs.append(sub)
        if temp==temp[::-1]:
                count += 1

print(f'{count} ({",".join(pairs)})')


