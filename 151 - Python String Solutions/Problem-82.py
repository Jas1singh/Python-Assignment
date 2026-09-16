# Problem 82: Create a string from a character array. 

# n = int(input("Enter no. of characters :"))

# ch = []

# print("Enter the Character :")
# for i in range(n):
#     ch.append(input())

ch = input("Enter the characters separated by spaces: ").split()

word = ""

for i in ch:
    word = word+i

print(word)

