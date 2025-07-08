def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1,2,5], 11))  # 3
