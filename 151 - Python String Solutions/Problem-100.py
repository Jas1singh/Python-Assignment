# Problem 100:

s1 = "abcx"
s2 = "abc."

def check(s):

    for i in range(len(s) - 2):

        if s[i] == 'a' and s[i + 1] == 'b' and s[i + 2] == 'c':

            if i + 3 == len(s) or s[i + 3] != '.':
                return True

    return False


print("S1:", check(s1))
print("S2:", check(s2))
