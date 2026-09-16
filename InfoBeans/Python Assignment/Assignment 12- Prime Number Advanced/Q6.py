# Assignment 12
# Question 6 : Next Prime Cabin Number Generator

n = int(input("Enter a Number : "))

num = n+1

while True:
    prime = True

    for i in range(2, num//2 + 1):
        if num % i== 0:
            prime = False
            break
        i+=1        
                  
    if prime:
        print("Next Prime Cabin:",num)
        break
    
    num +=1      