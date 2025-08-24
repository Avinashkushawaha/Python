def wordBreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[0] = True
    for i in range(1,len(s)+1):
        for w in wordDict:
            if dp[i-len(w)] and s[i-len(w):i]==w:
                dp[i] = True
    return dp[-1]

print(wordBreak("leetcode", ["leet","code"]))  # ✅ True
