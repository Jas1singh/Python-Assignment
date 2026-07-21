# Assignment 20
# Question 4 : Instant Messaging Word Encryption System

msg = input("Enter the message :")

words = msg.split()

encrypt = ""

for word in words:
    encrypt = encrypt + word[::-1]+" "

print("Encrypted Message:",encrypt)

