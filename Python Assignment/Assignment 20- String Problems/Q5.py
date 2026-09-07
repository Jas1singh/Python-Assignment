# Assignment 20
# Question 5 : Website URL Verification System

site = input("Enter the website :").lower()

if site.startswith("www") and site.endswith(".com"):
    print("Valid Website")

else:
    print("Invalid URL")