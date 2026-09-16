# Assignment 17
# Pattern 55 : 

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(1,i):
        print(" ", end="")

    for k in range(1,n+2-i):
            print(chr(64+k),end="") 
        
    print()