# Assignment 20
# Question 8 : SMART TEXT PROCESSING SYSTEM

while True:
    print("\n===== Smart Text Processing System =====")
    print("1. Reverse Complete String")
    print("2. Reverse Every Word")
    print("3. Reverse Word Order")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    # ---------------- Choice 1 ----------------
    if ch == 1:
        s = input("Enter String: ")

        letters = ""
        for c in s:
            if c.isalpha():
                letters += c

        rev = ""
        for i in range(len(letters) - 1, -1, -1):
            rev += letters[i]

        ans = ""
        k = 0
        for c in s:
            if c.isalpha():
                ans += rev[k]
                k += 1
            else:
                ans += c

        print("Output:", ans)

    # ---------------- Choice 2 ----------------
    elif ch == 2:
        s = " ".join(input("Enter String: ").split())
        words = s.split()

        out = ""

        for w in words:
            digit = False
            for c in w:
                if c.isdigit():
                    digit = True
                    break

            if digit:
                out += w + " "
            else:
                rev = ""
                for i in range(len(w) - 1, -1, -1):
                    rev += w[i]

                rev = rev[0].upper() + rev[1:].lower()
                out += rev + " "

        print("Output:", out.strip())

    # ---------------- Choice 3 ----------------
    elif ch == 3:
        s = input("Enter String: ")
        words = s.split()

        unique = []

        for w in words:
            found = False
            for u in unique:
                if u.lower() == w.lower():
                    found = True
                    break
            if not found:
                unique.append(w)

        out = ""
        for i in range(len(unique) - 1, -1, -1):
            out += unique[i].capitalize() + " "

        print("Output:", out.strip())

    # ---------------- Choice 4 ----------------
    elif ch == 4:
        print("Program Closed Successfully")
        break

    else:
        print("Invalid Choice")