def numWays(words, target):
    from collections import defaultdict
    mod = 10**9 + 7
    m, n = len(words[0]), len(target)
    dp = [0] * (n + 1)
    dp[0] = 1
    count = [defaultdict(int) for _ in range(m)]

    for word in words:
        for i, c in enumerate(word):
            count[i][c] += 1

    for i in range(m):
        for j in range(n - 1, -1, -1):
            dp[j + 1] += dp[j] * count[i][target[j]]
            dp[j + 1] %= mod
    return dp[n]
