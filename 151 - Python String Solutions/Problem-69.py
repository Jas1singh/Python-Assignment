# Problem 69: Count how many times 'life' appears in a string. 

s = input("Enter the String :")
word = input("Enter the Sub String :")

words = s.split()
count = 0 
for i in range(len(words)):
    if word == words[i]:
        count = count + 1
       
print(count) 

