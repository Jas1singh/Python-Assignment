# Problem 144:

s = "<a><b></a></b>"

stack = []
i = 0
valid = True

while i < len(s):

    if s[i] == '<':
        j = s.find('>', i)

        if j == -1:
            valid = False
            break

        tag = s[i+1:j]

        if tag.startswith('/'):
            name = tag[1:]

            if len(stack) == 0 or stack[-1] != name:
                valid = False
                break

            stack.pop()

        else:
            stack.append(tag)

        i = j + 1

    else:
        i += 1

if len(stack) != 0:
    valid = False

print(valid)
