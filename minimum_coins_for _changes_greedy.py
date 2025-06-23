def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

print(min_coins([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(min_coins([2], 3))         # Output: -1 (not possible             
