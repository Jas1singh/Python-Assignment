# Problem 116:

s1 = "xy"
s2 = "12"
s3 = "x1y2"

if len(s1) + len(s2) != len(s3):
    print(False)
else:
    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):

            if i > 0 and s1[i-1] == s3[i+j-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j]

            if j > 0 and s2[j-1] == s3[i+j-1]:
                dp[i][j] = dp[i][j] or dp[i][j-1]

    print(dp[len(s1)][len(s2)])
