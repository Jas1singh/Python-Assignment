# Problem 23: Print all characters that occur exactly twice.

s = input("Enter the String : ")
unique = ""
for i in s:
    c=0
    for j in s:
        if j == i:
            c+=1
    if c==2:
        if i not in unique:
            unique = unique + i
            print(i,end=" ")

