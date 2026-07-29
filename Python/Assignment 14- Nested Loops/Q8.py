# Assignment 14
# Question 8 : Online Exam Result Processing System

a = int(input("Enter number of classes :"))
b = int(input("Enter students per class :"))
c = int(input("Enter subjects per student :"))

# result = [[0 for j in range(students)] for i in range(classes)]

result = []
for i in range(a):
    row = []
    for j in range(b):
        row.append(0)
    result.append(row)

i = 1
while i<=a:
    print()
    print("Class ",i)
    
    j = 1
    while j<=b:
        print()
        print("Student ",j)
        total = 0
        

        k = 1
        while k<=c:
            mark = int (input("Enter the marks : "))
            total = total + mark
            k = k+1

        result[i][j] = total    
        j = j + 1
    i= i+1


    print("\nOutput:")

i = 1
while i <= a:
    print("\nClass", i)

    j = 1
    while j <= b:
        print("Student", j, "Total =", result[i][j])
        j += 1

    i += 1


