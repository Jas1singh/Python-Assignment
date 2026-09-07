# Assignment 17
# Pattern 27 : 

n = int(input("Enter the value of n : "))

for i in range(n):
    for j in range(n):
        if j == 0:
            print("1", end="")

        elif j==i or i == n-1:
            if j%2==0:
                print("1",end="")
            else:
                print("0",end="")    

        else:
            print(" ", end="")
    print()