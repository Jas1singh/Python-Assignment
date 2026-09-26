# Problem 131:

s = "test@example.com"

if s.count("@") == 1:
    a, b = s.split("@")

    if a != "" and b != "" and "." in b:
        if not b.startswith(".") and not b.endswith("."):
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)
