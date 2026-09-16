# Problem 36: Reverse order of words.

s = input("Enter the String : ")

words = s.split()

result = ""

for word in words:
    result = word +" "+ result 

print(result)

