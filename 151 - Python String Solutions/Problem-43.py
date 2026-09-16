# Problem 43: Check if two strings are rotations of each other. 

s1 = input("Enter the String1 : ")
s2 = input("Enter the String1 : ")

s3 = s1 + s1
# print(s3)

if len(s1)==len(s2) and s2 in s3:
    print(True)
else:
    print(False)    
   

