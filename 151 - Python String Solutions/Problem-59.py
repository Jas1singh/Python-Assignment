# Problem 59: Rotate characters right by 3 positions.

s = input("Enter the S :")

a = s[len(s)-3:]
b = s[:len(s)-3]

Result = a + b

print(Result)

