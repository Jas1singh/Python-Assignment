# Assignment 22
'''Question 5 : Cybercrime Log Analysis System
                A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.
If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a
'''

# s = input("Enter the string: ")

# last = ""

# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]==s[j]:
#             last = s[i]
#             break

# if last =="":
#     print("No reapeating character found")

# else:
#     print(last)   


# .................... Second Method...........................
    
s = input("Enter the string: ")

rev = s[::-1]

for ch in rev:
    if rev.count(ch)>1:
        print(ch)
        break

else:
    print("No repeating character found")    
