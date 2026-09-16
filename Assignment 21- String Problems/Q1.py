# Assignment 21
# Question 1 : Remove All Special Characters from a String

data = input("Enter the data :")

cleaned = ""

for ch in data:
    if ch.isspace() or ch.isalnum():
        cleaned = cleaned + ch

data = cleaned
print(data)


