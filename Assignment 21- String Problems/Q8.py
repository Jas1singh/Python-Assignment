# Assignment 21
''' Question 8 : Find the Second Highest Repeating Character in a String
                 Social Media Trend Analysis System '''

str = input("Enter the string :")

max1 = 0
max2 = 0

for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    if count > max1:
        max2 = max1
        max1 = count
    elif count > max2 and count != max1:
        max2 = count

printed = ""
for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    if count == max2 and i not in printed:
        print(i, end=" ")
        printed += i

