class Solution:
    def minCost(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + 1
                    
        return dp[n][m]
