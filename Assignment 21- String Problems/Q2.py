# Assignment 21
# Question 2 : Reverse Sentence + Reverse Each Word

sentence = input("Enter the sentence :")

# sentence = sentence[::-1]
# print(sentence)

words = sentence.split()

RevS = ""
Result = ""

for i in range(len(words)-1,-1,-1):
    RevS = RevS + (words[i]) + " "

for word in RevS.split():
    RevW = ""
    for i in range(len(word)-1,-1,-1):
        RevW = RevW + word[i]
    Result = Result + RevW + " "

print(Result)
