# Problem 98:

s1 = "zzyy"
s2 = "zyzz"

def check(s):

    for i in range(len(s)):
        if s[i] == 'z':
            if i + 1 < len(s) and s[i + 1] == 'z':
                return True
            else:
                return False

    return False


print("S1:", check(s1))
print("S2:", check(s2))
