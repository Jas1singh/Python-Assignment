# Assignment 14
# Question 4 : Armstrong Number Finder

a = int(input("Enter starting number :"))
b = int(input("Enter ending number : "))

for i in range(a, b+1):
      sum=0
      p = len(str(i))
      temp = i
      for j in range(1,temp+1):
        digit = temp % 10
        sum = sum + digit**p
        temp = temp // 10

      if sum == i and j>9 or j==1:
          print(i)
          