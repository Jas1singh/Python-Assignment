# Assignment 9
# Question 5 : Smart Farming Irrigation System

moisture = int(input("Enter the Soil Moisture : "))
crop = (input("Enter the Crop Type : ")).lower()

if moisture<=30:
    temperature = int(input("Enter the temperature : "))
    if temperature>=35:
        if crop=="wheat":
            print("Irrigation = High Water Supply")
        else:
            print("Irrigation = Moderate Water Supply")    
    
    else:
        print("Irrigation = Moderate Water Supply")

else:
    if moisture<=60:
        rainfall = input("Is there rainfall expected? (yes/no) : ").lower()
        if rainfall=="yes":
            print("Delay Irrigation")

        else:
            print("Irrigation = Light") 

    else:
        print("No Irrigation")          