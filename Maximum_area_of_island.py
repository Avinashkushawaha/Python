def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(i, j):
        if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + sum(dfs(i+di, j+dj) for di,dj in [(-1,0),(1,0),(0,-1),(0,1)])
    return max(dfs(i,j) for i in range(rows) for j in range(cols))
