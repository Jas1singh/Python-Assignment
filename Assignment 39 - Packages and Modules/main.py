from Number_System_Analysis import perfect_module,palindrome_module,strong_module,armstrong_module,prime_module,evenodd_module,factorial_module,sumDigits_module,reverse_module,countDigits_module,automorphic_module,neon_module,spy_module,harshad_module

while True:
    print(''' 
========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit
''')

    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            n = int(input("Enter a number : "))
            if perfect_module.isPerfect(n):
                print(n,"is a Perfect Number")  
            else:
                print(n,"is not a Perfect Number")

        case 2:
            n = int(input("Enter a number : ")) 

            if palindrome_module.isPalindrome(n):
                print(n,"is a Palindrom Number")  
            else:
                print(n,"is not a Palindrome Number")


        case 3:
            n = int(input("Enter a number : "))
           
            if strong_module.isStrong(n):
                print(n,"is a Strong Number")  
            else:
                print(n,"is not a Strong Number")


        case 4:
            n = int(input("Enter a number : "))
           
            if armstrong_module.isArmstrong(n):
                print(n,"is a Armstrong Number")  
            else:
                print(n,"is not Armstrong Number")


        case 5:
            n = int(input("Enter a number : "))
        
            if prime_module.isPrime(n):
                print(n,"is a Prime Number")  
            else:
                print(n,"is not Prime Number")


        case 6:
            n = int(input("Enter a number : "))
      
            if evenodd_module.isEvenOdd(n):
                print(n,"is a Even Number")  
            else:
                print(n,"is Odd Number")


        case 7:
            n = int(input("Enter a number : "))  
            print("Factorial of",n,"is: ",factorial_module.fact(n)) 


        case 8:
            n = int(input("Enter a number : "))
            print("Sum of digits : ",sumDigits_module.digitSum(n))


        case 9:
            n = int(input("Enter a number : "))
            print("Reverse of",n,"is : ",reverse_module.reverse(n)) 


        case 10:
            n = int(input("Enter a number : "))
            print("No. of digits in",n,": ",countDigits_module.digitCount(n)) 


        case 11:
            n = int(input("Enter a number : "))
        
            if automorphic_module.isAutomorphic(n):
                print(n,"is a Automorphic Number")  
            else:
                print(n,"is not a Automorphic Number")


        case 12:
            n = int(input("Enter a number : "))
          
            if neon_module.isNeon(n):
                print(n,"is a Neon Number")  
            else:
                print(n,"is not a Neon Number")


        case 13:
            n = int(input("Enter a number : "))
            
            if spy_module.isSpy(n):
                print(n,"is a Spy Number")  
            else:
                print(n,"is not a Spy Number")


        case 14:
            n = int(input("Enter a number : "))
        
            if harshad_module.isHarshad(n):
                print(n,"is a Harshad Number")  
            else:
                print(n,"is not a Harshad Number")


        case 15:
            print("Thank you for using Number Analysis System!")
            print("Program terminated.")
            break 


        case _:
           print("Invalid Choice!")
           print("Please select a choice between 1 and 15.")  
