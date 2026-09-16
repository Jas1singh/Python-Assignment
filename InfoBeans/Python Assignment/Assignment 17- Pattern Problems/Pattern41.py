# Assignment 17
# Pattern 41 : 

n = int(input("Enter number of rows: "))
ch = 65
j=0
for i in range(0,n):
      for j in range(0,2*i+1):
            print(chr(ch), end="") 
            ch+=1 
      print()