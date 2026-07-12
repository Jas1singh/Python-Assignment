# Assignment 17
# Pattern 38 : 


# n = int(input("Enter number of rows: "))

# for i in range(n, 0, -1):
#     if i == n or i <= 2:
#         for j in range(i):
#             print(i, end="")
#     else:
#         print(i, end="")
#         for j in range(i - 2):
#             print(" ", end="")
#         print(i, end="")
#     print()


n = int(input("Enter the value of n : "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        if i == n or j == 1 or j == i:
            print(i, end="")
        else:
            print(" ", end="")
    print()