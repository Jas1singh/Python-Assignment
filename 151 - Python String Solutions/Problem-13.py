# Problem 13:

s = input("Enter the String : ")
i = int(input("Enter the index : "))

print(ord(s[(i-1)]))


# s=input("Input")
# long=""

# for i in range(len(s)):
#     temp=""
#     for j in range(i,len(s)):
#             temp+=s[j]
#             print("sub",temp)
#             c=0
#             for k in range(len(s)-len(temp)+1):
#              if s[j:k]==temp[k]:
#                  print("substring",s[j:k])
#                  c+=1
#             if c >= 2 and len(temp) > len(long):
#                long = temp    
# print("Longest String",long)