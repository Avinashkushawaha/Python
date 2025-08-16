def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0]*(n+1)
    for i in range(1, n+1):
        cur_max = 0
        for l in range(1, min(k, i)+1):
            cur_max = max(cur_max, arr[i-l])
            dp[i] = max(dp[i], dp[i-l] + cur_max*l)
    return dp[n]

# print(maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))  # 84
