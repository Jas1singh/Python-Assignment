# Problem 132:

s = "192.168.1.1"

parts = s.split(".")

valid = True

if len(parts) != 4:
    valid = False
else:
    for part in parts:
        if part == "":
            valid = False
            break

        if not part.isdigit():
            valid = False
            break

        if len(part) > 1 and part[0] == '0':
            valid = False
            break

        if int(part) < 0 or int(part) > 255:
            valid = False
            break

print(valid)
