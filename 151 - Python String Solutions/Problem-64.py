# Problem 64:  Count frequency of each vowel.

s = input("Enter the String :")
visited = ""
vowels = "aeiou"

for i in vowels:
    c = 0
    if i not in visited:
        for j in s:
            if i == j:
                c+=1
        print(i,":",c)
        visited = visited + i

