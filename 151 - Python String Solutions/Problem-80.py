# Problem 80:  Print list items containing all characters of a given word.

s = input("Enter the items :").split()

word = input("Enter the word :")

result = []
found = False
for w in s:
    for ch in word:
        if ch in w:
            found = True

    if found:
        result.append(w)

if not found:
    print("No items matching with word")       

else:
    print(result)        

                  

    