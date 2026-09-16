# Assignment 7
# Question 6 : Armstrong Number

num = int(input("Enter number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")



# num = int(input("Enter number: "))

# for i in range(1,num+1):
#     original = i
#     sum = 0
#     while i > 0:
#         digit = i % 10
#         sum = sum + digit ** 3
#         i = i // 10

#     if original == sum:
#         print(original,end=" ")

