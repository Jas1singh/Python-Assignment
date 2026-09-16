# Problem 62: Count vowels and consonants. 

s = input("Enter the String :")

c1 = 0
c2 = 0

vowel = "aeiouAIEOU"
for i in s:
    if i in vowel:
        c1+=1

    else:
        c2+=1 

print("Vowels :",c1)               
print("Consonants :",c2)
