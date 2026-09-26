# Problem 145:

s = "<h1>Title</h1>"

result = ""
inside = False

for ch in s:

    if ch == '<':
        inside = True

    elif ch == '>':
        inside = False

    elif not inside:
        result += ch

print(result)
