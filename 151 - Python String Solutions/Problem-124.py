# Problem 124:

s1 = "AGGTAB"
s2 = "GXTXAYB"

m = len(s1)
n = len(s2)

dp = [[""] * (n + 1) for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[m][n])
