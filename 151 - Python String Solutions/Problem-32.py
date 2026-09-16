# Problem 32: Count frequency of each word.

s = input("Enter the String : ")
words = s.split()

visited=""

for w in words:
    if w not in visited:
        count = 0
        for word in words:
            if w==word:
                count+=1
        print(w,":",count)
        visited = visited + w
print(visited)              

