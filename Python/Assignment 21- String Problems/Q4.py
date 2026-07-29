# Assignment 21
''' Question 4 : Program should work for both uppercase and lowercase letters.
                 Find the Shortest Word in a Sentence
                 Telecom SMS Cost Optimization System  '''


str = input("Enter the Enter the string:")

words = str.split()
max = len(str)
shortWord = ""

for word in words:
     length = (len(word))

     if length < max:
          max = length
          shortWord = word

print(shortWord)
     

