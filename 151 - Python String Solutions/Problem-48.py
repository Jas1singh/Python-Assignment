# Problem 48:  Remove all vowels

s = input("Enter the String :")

for i in s:
    if i in "aieou":
        continue

    else:
        print(i,end="")
