# Assignment 17
# Pattern 23 : 

n = int(input("Enter the value of n : "))
k=0
for i in range(n):
    for j in range(0,i+1):
        if i == n-1 or j == 0 or j == i:
            print(chr(97+k), end="")
            
        else:
            print(" ", end="")  
        k+=1         
    print()