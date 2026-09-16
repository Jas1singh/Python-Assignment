# Problem 21: Find the first non-repeating character.

s = input("Enter the String : ")

for i in s:
    c=0
    for j in s:
        if j == i:
            c+=1
    if c==1:
        print(i)
        break