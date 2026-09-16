# Problem 47: Check for substring using concatenation trick.

s1 = input("Enter the String1 : ")
s2 = input("Enter the String2 : ")

s3 = s2+s2

if s1 in s3:
    print("True")

else:
    print("False")



