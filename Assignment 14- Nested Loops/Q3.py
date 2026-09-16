# Assignment 14
# Question 3 : Prime Number Range Checker

a = int(input("Enter starting number :"))
b = int(input("Enter ending number : "))

for i in range(a, b+1):
      if i>1:
          for j in range(2, i//2+1):
              if i % j == 0:
                  break
          else:
              print(i)    

