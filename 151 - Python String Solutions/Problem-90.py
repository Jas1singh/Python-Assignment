# Problem 90:

s = "azxxzy"

def remove_duplicates(s):
    if len(s) == 0:
        return s

    result = ""
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            ch = s[i]

            while i < len(s) and s[i] == ch:
                i += 1
        else:
            result += s[i]
            i += 1

    if result == s:
        return result

    return remove_duplicates(result)

print(remove_duplicates(s))
