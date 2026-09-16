# Problem 75:  Find the longest common prefix among strings.

s = input("Enter the String :")
p = []

words = s.split()

for i in range(len(words)-1):
    prefix = ""
    for j in range(min(len(words[i]),len(words[i+1]))):
        if words[i][j]==words[i+1][j]:
            prefix = prefix + words[i][j]
   
    p.append(prefix)                 

print(f'{p}')

minPrefix = p[0]
for i in p:
    min = len(p[0])
    if len(i) < min:
            min = len(i)
            minPrefix = i
            
print(f'Longest common prefix : {minPrefix}')

