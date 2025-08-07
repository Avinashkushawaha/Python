def min_cuts_palindrome(s):
    n = len(s)
    dp = [0] * n
    pal = [[False]*n for _ in range(n)]
    
    for i in range(n):
        min_cut = i
        for j in range(i+1):
            if s[j] == s[i] and (i-j <= 2 or pal[j+1][i-1]):
                pal[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, dp[j-1] + 1)
        dp[i] = min_cut
    return dp[-1]

