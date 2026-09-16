# Problem 24:  Check if all characters in a string are unique.   

s1 = input("Enter the String : ")
s2 = input("Enter the String : ")

unique1 = ""
unique2 = ""

for i in s1:
     if i not in unique1:
         unique1 = unique1 + i

for i in s2:
     if i not in unique2:
         unique2 = unique2 + i

if len(s1)==len(unique1) and len(s2)!=len(unique2):
    print("S1:True , S2:False")

elif len(s1)!=len(unique1) and len(s2)==len(unique2):
    print("S1:False , S2:True")

else:
    print("S1:False , S2:False")