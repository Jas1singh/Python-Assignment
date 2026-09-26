# Problem 83: Create a string from a byte array

byte = [72, 101, 108]

s = ""

for x in byte:
    s += chr(x)

print(s)
