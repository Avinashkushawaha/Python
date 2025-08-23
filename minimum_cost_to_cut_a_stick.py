def minCost(n, cuts):
    cuts = sorted(cuts)
    cuts = [0] + cuts + [n]
    m = len(cuts)
    dp = [[0]*m for _ in range(m)]
    for l in range(2, m):
        for i in range(m-l):
            j = i+l
            dp[i][j] = min(dp[i][k]+dp[k][j] for k in range(i+1,j)) + cuts[j]-cuts[i]
    return dp[0][-1]

print(minCost(7, [1,3,4,5]))
