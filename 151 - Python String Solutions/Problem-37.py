# Problem 37: Reverse each word.

s = input("Enter the String : ")

words = s.split()

result = ""

for word in words:
    result = result + word[::-1] +" "

print(result)