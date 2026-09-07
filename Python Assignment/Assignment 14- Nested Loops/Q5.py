# Assignment 14
# Question 5 : Strong Number Detector

a = int(input("Enter starting number :"))
b = int(input("Enter ending number : "))

for i in range(a, b+1):
      sum = 0
      temp = i
      
      while temp>0:
            digit = temp % 10
            
            fact = 1
            for j in range(1,digit+1):
                 fact = fact * j

            sum = sum + fact     
            temp = temp // 10

      if sum == i:
          print(i)
          