# Problem 93:

pattern = "a?c"
text = "axcde"

def match(pattern, text):

    if len(pattern) == 0:
        return len(text) == 0

    if pattern[0] == '*':
        return (
            match(pattern[1:], text) or
            (len(text) > 0 and match(pattern, text[1:]))
        )

    if len(text) == 0:
        return False

    if pattern[0] == '?' or pattern[0] == text[0]:
        return match(pattern[1:], text[1:])

    return False


print(match(pattern, text))
