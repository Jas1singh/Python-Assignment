# Problem 49: Replace all consonants with '*' (Example suggests replacing non-vowels).

s = input("Enter the String :").lower()

for i in s:
    if i in "aieou":
        print(i,end="")

    else:
        print("*",end="")

