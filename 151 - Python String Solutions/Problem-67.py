# Problem 67:  Count how many times a substring appears. 

s = input("Enter the String :")
sub = input("Enter the Sub String :")

count = 0
for i in range(len(s)-len(sub)+1):
    match = 1
    for j in range(len(sub)):
        if s[i+j]!=sub[j]:
            match = 0
            break

    if match == 1:
        count = count + 1

print(count)            




