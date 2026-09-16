# Problem 71: Print all substrings.

s = input("Enter the String :")
count = 0
pairs = []

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        pairs.append(sub)

print(f'({",".join(pairs)})')

