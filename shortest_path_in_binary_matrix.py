from collections import deque

def shortest_path_binary_matrix(grid):
    if grid[0][0] or grid[-1][-1]: return -1
    n = len(grid)
    q = deque([(0, 0, 1)])
    dirs = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]
    
    while q:
        x, y, dist = q.popleft()
        if x == y == n - 1:
            return dist
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny]:
                grid[nx][ny] = 1
                q.append((nx, ny, dist + 1))
    return -1