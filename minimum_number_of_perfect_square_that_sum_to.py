import math

def numSquares(n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)
    return dp[n]

print(numSquares(12))  # Output: 3 (4+4+4)
print(numSquares(13))  # Output: 2 (4+9)
