def strangePrinter(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            dp[i][j] = dp[i+1][j] + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
    return dp[0][n-1]
