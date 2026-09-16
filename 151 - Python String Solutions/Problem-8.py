# Problem 8:

s = input("Enter the String : ")

# print(s.swapcase())

for ch in s:
    if ch==ch.upper():
        print(ch.lower(),end="")
    else:
        print(ch.upper(),end="")    