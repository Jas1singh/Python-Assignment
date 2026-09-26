# Problem 125:

s1 = "AGGTAB"
s2 = "GXTXAYB"

m = len(s1)
n = len(s2)

dp = [[""] * (n + 1) for i in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = s1[:i]

for j in range(n + 1):
    dp[0][j] = s2[:j]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            a = dp[i-1][j] + s1[i-1]
            b = dp[i][j-1] + s2[j-1]

            if len(a) <= len(b):
                dp[i][j] = a
            else:
                dp[i][j] = b

print(dp[m][n])
