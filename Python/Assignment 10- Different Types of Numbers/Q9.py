# Assignment 10
# Question 9 : Step Difference Number Analyzer

num = input("Enter the Number : ")

step = ""
total = 0
largest = 0

for i in range(len(num) - 1):
    diff = abs(int(num[i]) - int(num[i + 1]))
    step = step + str(diff)

    total = total + diff

    if diff > largest:
        largest = diff

print("Step Differences:", end=" ")

for x in step:
    print(x, end=" ")
print()

print("Sum =", total)
print("Largest =", largest)

if total % len(num) == 0:
    print("Balanced Number")
    
else:
    print("Unbalanced Number")