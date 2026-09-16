# Problem 66:  Count number of sentences in a paragraph. 

s = input("Enter the string :")

count = 0
for i in s:
    if i==".":
        count = count + 1
print(count)        

