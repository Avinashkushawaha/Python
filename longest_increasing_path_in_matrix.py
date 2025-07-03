def longest_increasing_path(matrix):
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0]*n for _ in range(m)]

    def dfs(r, c):
        if memo[r][c]:
            return memo[r][c]
        val = matrix[r][c]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > val:
                memo[r][c] = max(memo[r][c], dfs(nr, nc))
        memo[r][c] += 1
        return memo[r][c]

    return max(dfs(i, j) for i in range(m) for j in range(n))
