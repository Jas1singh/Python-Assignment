# Assignment 17
# Pattern 12 : 

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(i):
        print(chr(97+j),end="")
    print() 
