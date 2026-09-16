# Problem 22: Find the last repeating character.

s = input("Enter the String : ")
unique = ""
for i in s:
    c=0
    for j in s:
        if j == i:
            c+=1
    if c>1:
        unique = unique + i
        
print(unique[-1])


# last non-repeating character.

# print(unique[-1])
# s = input("Enter the String : ")
# unique = ""
# for i in s:
#     c=0
#     for j in s:
#         if j == i:
#             c+=1
#     if c==1:
#         unique = unique + i

# print(unique[-1])