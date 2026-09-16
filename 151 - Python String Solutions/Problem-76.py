# Problem 76: Find the longest common suffix among strings.

s = input("Enter the String :")
p = []

words = s.split()

for i in range(len(words)-1,0,-1):
    suffix = ""
    for j in range(1,min(len(words[i]),len(words[i-1]))+1):
        if words[i][-j]==words[i-1][-j]:
            suffix = words[i][-j] + suffix
   
    p.append(suffix)                 

print(f'{p}')

minSuffix = p[0]
for i in p:
    min = len(p[0])
    if len(i) < min:
            min = len(i)
            minSuffix = i
            
print(f'Longest common suffix : {minSuffix}')