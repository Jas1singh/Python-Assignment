# Assignment 11
# Question 2 : Next Prime ID Generator

n = int(input())

num = n + 1


if num <= 1:
    print("Not Prime")

else:
    for i in range(2, num//2 + 1):
         if num % i == 0:
            print("Next Not Prime =", num)
            break
         
    else:
        print("Next Prime =", num)