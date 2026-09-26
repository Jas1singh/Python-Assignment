# Problem 104:

s = "{[()]}"

stack = []

for ch in s:
    if ch in "([{":
        stack.append(ch)

    elif ch in ")]}":
        if len(stack) == 0:
            print(False)
            break

        top = stack.pop()

        if (ch == ')' and top != '(') or \
           (ch == ']' and top != '[') or \
           (ch == '}' and top != '{'):
            print(False)
            break
else:
    print(len(stack) == 0)
