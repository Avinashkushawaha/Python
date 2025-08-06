from collections import deque

def shortest_path_with_obstacles(grid, k):
    m, n = len(grid), len(grid[0])
    visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
    queue = deque([(0, 0, 0, 0)])  # x, y, steps, obstacles_removed

    while queue:
        x, y, steps, obs = queue.popleft()
        if x == m - 1 and y == n - 1:
            return steps
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                n_obs = obs + grid[nx][ny]
                if n_obs <= k and not visited[nx][ny][n_obs]:
                    visited[nx][ny][n_obs] = True
                    queue.append((nx, ny, steps + 1, n_obs))
    return -1

# Example:
grid = [[0,1,1],[1,1,0],[1,1,0]]
k = 1
print(shortest_path_with_obstacles(grid, k))  # Output: -1
