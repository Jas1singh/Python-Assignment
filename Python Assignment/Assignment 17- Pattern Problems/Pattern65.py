# Assignment 17
# Pattern 65 : 

n = int(input("Enter the value of n : "))

for i in range(0,n):
    for j in range(1,n-i+1):
        print(" ", end="")

    for k in range(0,i+1):
        if i==0 or k==0 or k==i or i<n-3:
            print("1", end=" ")

        elif i==n-3 and k<=i-1:
             print("2",end=" ")

        elif i==n-2 and k<i:
             print("3",end=" ") 

        elif i==n-1:
                if k%2==0:
                     print("6",end=" ")
                else:
                     print("4",end=" ")       

        else:
            print(" ",end="")    
               
              
    print()