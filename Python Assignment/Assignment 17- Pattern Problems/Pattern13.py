# Assignment 17
# Pattern 13 : 

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(i):   
            print((i+j)%2,end="")
            
    print() 
