# Problem 63:  Count frequency of each character.

s = input("Enter the String :")
visited = ""

for i in s:
    c = 0
    if i not in visited:
        for j in s:
            if i == j:
                c+=1
        print(i,":",c)
        visited = visited + i


