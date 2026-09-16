# Problem 70:  Compare the number of times 'the' and 'is' appear.

s = input("Enter the String :")
words = s.split()

visited = []
word =""
for i in words:
    if i=="the" or i=="is":
        c = 0
        if i not in visited:
            for j in words:
                if i == j:
                    c+=1

            print(i,":",c,end=", ")
            word = word+i
            visited.append(i)

print(f"({word})")          

