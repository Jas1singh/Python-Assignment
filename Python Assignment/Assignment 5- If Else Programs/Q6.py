# Assignment 5
# Question 6 : Weather Monitorinng System

temperature = int(input("Enter the temperature value : "))

if temperature>=30:
    humidity = int(input("Enter the humidity value : "))
    if humidity>=70:
        print("Hot day")
        print("High Humidity alert")

    else:
        print("Hot day")
        print("Low Humidity")

else:
    print("Normal day")

