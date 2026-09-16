# Assignment 17
# Pattern 15 : 

n = int(input("Enter the value of n : "))
ch =65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
    ch = ch+1
    print() 
