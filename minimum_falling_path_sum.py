def minFallingPathSum(grid):
    n = len(grid)
    dp = grid[0][:]
    for i in range(1, n):
        min1, min2 = sorted((v, j) for j, v in enumerate(dp))[:2]
        new = [0] * n
        for j in range(n):
            if j == min1[1]:
                new[j] = grid[i][j] + min2[0]
            else:
                new[j] = grid[i][j] + min1[0]
        dp = new
    return min(dp)

print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
