# Problem 31: Remove duplicate words.

s = input("Enter the String : ")

words = s.split()
result =""

for word in words:
    if word not in result:
        result+=word+" "

print(result) 

