# Problem 54: Replace duplicate chars with '$'.

# s = input("Enter String :")
# result = ""

# for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             result = result + "$"
#         else:
#             result = result + s[i]
                
# print(result+s[-1])


s = input("Enter String :")
result = ""

for i in range(len(s)):
        if i+1<len(s) and s[i]==s[i+1]:
            result = result + "$"
        else:
            result = result + s[i]
                
print(result)




