def cherry_pickup(grid):
    n = len(grid)
    dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
    def dfs(x1, y1, x2):
        y2 = x1 + y1 - x2
        if x1 >= n or y1 >= n or x2 >= n or y2 >= n or \
           grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -float('inf')
        if x1 == y1 == x2 == y2 == n - 1:
            return grid[x1][y1]
        if dp[x1][y1][x2] != -1:
            return dp[x1][y1][x2]
        res = grid[x1][y1]
        if x1 != x2 or y1 != y2:
            res += grid[x2][y2]
        res += max(
            dfs(x1+1, y1, x2+1), dfs(x1+1, y1, x2),
            dfs(x1, y1+1, x2+1), dfs(x1, y1+1, x2)
        )
        dp[x1][y1][x2] = res
        return res
    return max(0, dfs(0, 0, 0))
