def num_islands(grid):
    if not grid: return 0 
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j>=n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        for dx, dy in[(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(i+dx, j+dy)

    count = 0 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
                count += 1 
    return count            
