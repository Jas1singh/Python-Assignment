# Problem 44: Check if two strings are anagrams.

s1 = input("Enter the String1 : ").lower()
s2 = input("Enter the String1 : ").lower()

str1 =""
str2 =""

for ch in s1:
    if not ch.isspace():
        str1+=ch

for ch in s2:
    if not ch.isspace():
        str2+=ch

str1 = sorted(s1)
str2 = sorted(s2)

if len(str1)==len(str2):
    # c1=0
    # c2=0
    # anagram = False

    # for i in range(len(s1)):
        
    #     for j in range(len(s2)):
    #         if s1[i]==s2[j]:
    #             c1 = c1 + 1

    #     for j in range(len(s2)):
    #         if s1[i]==s2[j]:
    #             c2 = c2 + 1
                
    #     if c1==c2:
    #         anagram = True
    #         break

    if str1==str2:
        print("Anagram")

    else:
        print("Not anagram")           

else:
    print("Not anagram")   

