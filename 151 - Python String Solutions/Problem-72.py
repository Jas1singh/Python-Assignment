# Problem 72: Print all substrings of length n. 

s = input("Enter the String :")
count = 0
pairs = []

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        if len(sub)==2:
            pairs.append(sub)

print(f'({",".join(pairs)})')

