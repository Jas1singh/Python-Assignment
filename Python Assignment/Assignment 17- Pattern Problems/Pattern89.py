# Assignment 17
# Pattern 89 : 

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")


    for j in range(1,2*i):
        if j%2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()