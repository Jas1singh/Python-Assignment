# Assignment 17
# Pattern 88 : 


n = int(input("Enter the value of n : "))

for i in range(1, n):
    for j in range(1,n):
        print(" ", end="")
    print(i)


for i in range(1, n + 1):
    print(i, end="")
for i in range(n - 1, 0, -1):
    print(i, end="")
print()


for i in range(n - 1, 0, -1):
    for j in range(1,n):
        print(" ", end="")
    print(i)