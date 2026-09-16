# Problem 45: Check whether a string starts/ends with another string.

s = input("Enter the String : ")
prefix = input("Enter the Prefix: ")
suffix = input("Enter the Suffix : ")

words = s.split()

if words[0]==prefix and words[-1]==suffix:
    print("Start: True , End : True")

elif words[0]!=prefix and words[-1]==suffix:
    print("Start: False , End : True")

elif words[0]==prefix and words[-1]!=suffix:
    print("Start: True , End : False")

else:
    print("Start: False , End : False")

