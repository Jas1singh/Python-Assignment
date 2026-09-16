# Assignment 17
# Pattern 63 : 

n = int(input("Enter the value of n : "))

for i in range(0,n):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,2*i+1):
        print(chr(65+k), end="") 

    print()