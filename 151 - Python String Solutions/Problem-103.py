# Problem 103:

s = "((()))"

count = 0
valid = True

for ch in s:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1

    if count < 0:
        valid = False
        break

if count != 0:
    valid = False

print(valid)

