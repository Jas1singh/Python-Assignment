# Assignment 17
# Pattern 39 : 

n = int(input("Enter number of rows: "))
limit = n

for i in range(1,n+1):
        if i%2==1:
             for j in range(1,limit+1):
                   print(j, end="")
        else:
              for j in range(limit,0,-1):
                    print(j,end="")
        print()
        limit = limit - 1   