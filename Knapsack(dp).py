def knapsack(weights, values, w):
    n= len(weights)
    dp = [[0]*(w+1) for _ in range(n+1)]
    for i in range(n):
        for w in range(w+1):
            if weights[i] <= w:
                dp[i+1][w] = max(dp[i][w], dp[i][w-weights[i]] + values[i])
            else:
                dp[i+1][w] = dp[i][w]

    return dp[n][w]
                