# Assignment 14
# Question 7 : Neon Number Detector

a = int(input("Enter starting number :"))
b = int(input("Enter ending number : "))

for i in range(a, b+1):
      sum=0
      square = i * i
      temp = square

      for j in range(len(str(square))):
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10

      if sum == i:
          print(i)
          