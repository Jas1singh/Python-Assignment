# Problem 18:

s = input("Enter the String : ")
old = input("Enter the old character : ")
new = input("Enter the new character : ")

# print(s.replace(old,new))

for c in s:
    if c==old:
        print(new,end="")
    else:
        print(c,end="")    
