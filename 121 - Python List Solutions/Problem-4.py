#''' Problem 4: Search Insert Position'''

size = int(input("Enter the size of list : "))

a = []

for i in range(size):
    a.append(int(input()))

target = int(input("Enter the value to search : "))

print("Output : ")

if target in a:
    for i in range(len(a)):
        if a[i]==target:
            print(i)
            break

elif target not in a:
     for i in range(size):
        if a[i]==target-1:
            print(i+1)
            break    

        elif a[i]==target+1:
            print(i)
            break 
            

 

