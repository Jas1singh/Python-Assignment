# Assignment 13
# Question 1 : Utility Toolkit System

while True:
    print("\n1. Check Prime Number")
    print("2. Check Palindrome Number")
    print("3. Reverse a Number")
    print("4. Count Digits")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            num = int(input("Enter number: "))
            n = abs(num)

            if n < 2:
                print(num, "is not a Prime Number")
            else:
                prime = True
                i = 2
                while i <= n // 2:
                    if n % i == 0:
                        prime = False
                        break
                    i += 1

                if prime:
                    print(num, "is a Prime Number")
                else:
                    print(num, "is not a Prime Number")

        case 2:
            num = int(input("Enter number: "))
            n = abs(num)
            temp = n
            rev = 0

            while temp > 0:
                digit = temp % 10
                rev = rev * 10 + digit
                temp //= 10

            if rev == n:
                print(num, "is a Palindrome Number")
            else:
                print(num, "is not a Palindrome Number")

        case 3:
            num = int(input("Enter number: "))
            sign = 1
            if num<0:
                sign = sign * -1
            else:
                sign = sign * 1

            n = abs(num)

            rev = 0
            while n > 0:
                digit = n % 10
                rev = rev * 10 + digit
                n //= 10

            print("Reversed Number is:", sign * rev)

        case 4:
            num = int(input("Enter number: "))
            n = abs(num)

            if n == 0:
                count = 1
            else:
                count = 0
                while n > 0:
                    count += 1
                    n //= 10

            print("Total digits:", count)

        case 5:
            print("Exiting program... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

