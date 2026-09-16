# Assignment 21
''' Question 3 : Find the First Non-Repeated Character 
                 Railway Ticket Fraud Detection System '''


ticketID = input("Enter the Ticket ID :")


for i in range(len(ticketID)):
    once = True
    for j in range(len(ticketID)):
        if i!=j and ticketID[i]==ticketID[j]:
            once = False
            break
    if once:
        print(ticketID[i])
        break

else:
    print("No non-repeating character found")
