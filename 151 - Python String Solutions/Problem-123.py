# Problem 123:

n = 5

if n == 0:
    print("0")
else:
    binary = ""

    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    print(binary)
