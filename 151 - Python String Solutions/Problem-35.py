# Problem 35: Find the first palindrome word.

s = input("Enter the String : ")

words = s.split()

result = ""

for word in words:
    if word==word[::-1]:
        result = word
        break

print(result)

