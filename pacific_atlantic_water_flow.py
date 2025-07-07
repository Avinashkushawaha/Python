def pacific_atlantic(heights):
    if not heights: return []
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prev_height):
        if (r, c) in visited or r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < prev_height:
            return
        visited.add((r, c))
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r+dr, c+dc, visited, heights[r][c])

    for i in range(m):
        dfs(i, 0, pac, heights[i][0])
        dfs(i, n-1, atl, heights[i][n-1])
    for j in range(n):
        dfs(0, j, pac, heights[0][j])
        dfs(m-1, j, atl, heights[m-1][j])

    return list(pac & atl)
