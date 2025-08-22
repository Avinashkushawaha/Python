def knightProbability(N, K, r, c):
    moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    dp = [[0]*N for _ in range(N)]
    dp[r][c] = 1
    for _ in range(K):
        ndp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if dp[i][j]:
                    for dx,dy in moves:
                        x,y = i+dx, j+dy
                        if 0<=x<N and 0<=y<N:
                            ndp[x][y] += dp[i][j]/8
        dp = ndp
    return sum(map(sum,dp))
