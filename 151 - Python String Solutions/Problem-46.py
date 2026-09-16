# Problem 46: Check if a substring appears at both the start and end. 

s = input("Enter the String : ")
sub = input("Enter the Sub String : ")

start = ''
end = ''

for i in range(len(sub)):
    start = start + s[i]

for i in range(len(s)-len(sub),len(s)):
    end = end + s[i]

# start = s[:length]
# end = s[-length:] 

print(start)
print(end)


if sub==start and sub==end:
    print("True")
else:
    print("False")