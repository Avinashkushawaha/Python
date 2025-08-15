def minFallingPathSumII(grid):
    n = len(grid)
    INF = 10**15
    dp = grid[0][:]
    for r in range(1, n):
        # track smallest and second smallest from previous row
        min1 = min2 = (INF, -1)
        for c, v in enumerate(dp):
            if v < min1[0]:
                min2 = min1
                min1 = (v, c)
            elif v < min2[0]:
                min2 = (v, c)
        ndp = [0]*n
        for c in range(n):
            best_prev = min1[0] if c != min1[1] else min2[0]
            ndp[c] = grid[r][c] + best_prev
        dp = ndp
    return min(dp)

# print(minFallingPathSumII([[1,2,3],[4,5,6],[7,8,9]]))  # 13
