# Assignment 15
# Question 6 : 

n = int(input("Enter the no. of lines : "))

for i in range(1,n+1):
    print()
    for j in range(i):
        print(chr(97 + j), end="") 