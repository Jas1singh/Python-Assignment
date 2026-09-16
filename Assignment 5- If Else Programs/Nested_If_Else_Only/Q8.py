# Assignment 5
# Question 8 : A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.


unit1 = int(input("Enter no. of units 1 : "))
unit2 = int(input("Enter no. of units 2: "))
unit3 = int(input("Enter no. of units 3: "))
unit4 = int(input("Enter no. of units 4: "))
unit5 = int(input("Enter no. of units 5: "))
unit6 = int(input("Enter no. of units 6: "))

if unit1>unit2:
    if unit1>unit3:
        if unit1>unit4:
            if unit1>unit5:
                if unit1>unit6:
                    print("Highest Stock = ",unit1)
                else:
                    print("Highest Stock = ",unit6)   
            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)

                else:
                    print("Highest Stock = ",unit6)   

        else:
            if unit4>unit5:
                if unit4>unit6:
                    print("Highest Stock = ",unit4)

                else:
                    print("Highest Stock = ",unit6)

            else:
                print("Highest Stock = ",unit5) 

    else:
        if unit3>unit4:
            if unit3>unit5:
                if unit3>unit6:
                    print("Highest Stock = ",unit3)
                else:
                    print("Highest Stock = ",unit6)

            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)
                else:
                    print("Highest Stock = ",unit6)    
        
        else:
            if unit4>unit5:
                if unit4>unit6:
                    print("Highest Stock = ",unit4)
                else:
                    print("Highest Stock = ",unit6)    

            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)
                else:
                    print("Highest Stock = ",unit6)    


else:
    if unit2>unit3:
        if unit2>unit4:
            if unit2>unit5:
                if unit2>unit6:
                    print("Highest Stock = ",unit2)
                else:
                    print("Highest Stock = ",unit6)
            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)
                else:
                    print("Highest Stock = ",unit6)

        else:
            if unit4>unit5:
                if unit4>unit6:
                    print("Highest Stock = ",unit4)
                else:
                    print("Highest Stock = ",unit6)                                

            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)
                else:
                    print("Highest Stock = ",unit6)           

    else:
        if unit3>unit4:
            if unit3>unit5:
                if unit3>unit6:
                    print("Highest Stock = ",unit3)
                else:
                    print("Highest Stock = ",unit6) 
            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)
                else:
                    print("Highest Stock = ",unit6) 

        else:
            if unit4>unit5:
                if unit4>unit6:
                    print("Highest Stock = ",unit6)
                else:
                    print("Highest Stock = ",unit4)  

            else:
                if unit5>unit6:
                    print("Highest Stock = ",unit5)
                else:
                    print("Highest Stock = ",unit6)
                                                                           