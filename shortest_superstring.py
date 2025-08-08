class Solution:
    def shortestSuperstring(self, A):
        n = len(A)
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    for k in range(min(len(A[i]), len(A[j])), -1, -1):
                        if A[i].endswith(A[j][:k]):
                            overlap[i][j] = k
                            break
        
        dp = [[""]*n for _ in range(1<<n)]
        for i in range(n):
            dp[1<<i][i] = A[i]
        
        for mask in range(1<<n):
            for j in range(n):
                if not (mask & (1<<j)):
                    continue
                for k in range(n):
                    if j == k or not (mask & (1<<k)):
                        continue
                    cand = dp[mask^(1<<j)][k] + A[j][overlap[k][j]:]
                    if dp[mask][j] == "" or len(cand) < len(dp[mask][j]):
                        dp[mask][j] = cand
                        
        return min(dp[-1], key=len)
