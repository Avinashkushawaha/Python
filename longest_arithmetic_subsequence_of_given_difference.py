def longestSubsequence(arr, diff):
    dp = {}
    res = 0
    for x in arr:
        dp[x] = dp.get(x-diff, 0) + 1
        res = max(res, dp[x])
    return res

print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))
