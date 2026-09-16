# Assignment 22
''' Question 1 : Find the Longest Substring Without Repeating Characters
                 Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.
To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc 
'''

s = input("Enter the String :")
count = 0
pairs = []
max = 0
maxSub =""
nonRepeat = ""

for i in range(len(s)):
     for j in range(i+1,len(s)+1):
        sub = s[i:j]
        match=1
        for k in range(len(sub)):
             if k+1<len(sub) and sub[k]==sub[k+1]:
                    match = 0
                    break
        if match ==1:
             pairs.append(sub)

for i in range(len(pairs)):
    for j in range(len(pairs[i])):
        if len(pairs[i])>max:
            maxSub = pairs[i]
            max = len(pairs[i])
            for w in maxSub:
                 if w not in nonRepeat:
                      nonRepeat = nonRepeat + w

print(f'{nonRepeat}')


# str = input("Enter the String : ")

# max = 0
# longest = ""

# words = str.split()

# for word in words:
#     if len(word)>max:
#         longest = word
#         max = len(longest)

# cleaned = ""

# for w in longest:
#     if w not in cleaned:
#         cleaned = cleaned + w
# print(cleaned)     



