# Assignment 20
# Question 3 : Smart Chat Message Cleaner

msg = input("Enter the message :")

words = msg.split()

cleaned = ""

for word in words:
    cleaned = cleaned + word.strip()+" "

print("Cleaned Message:",cleaned)