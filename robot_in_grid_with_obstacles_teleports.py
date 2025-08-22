from collections import deque

def minSteps(grid, start, end, teleports):
    n, m = len(grid), len(grid[0])
    teleport_map = {t[0]: t[1] for t in teleports}
    q = deque([(start[0], start[1], 0)])
    visited = set([start])
    
    while q:
        x, y, steps = q.popleft()
        if (x, y) == end:
            return steps
        if (x, y) in teleport_map:
            nx, ny = teleport_map[(x, y)]
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, steps + 1))
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny,steps+1))
    return -1

grid = [[0,0,0],[1,1,0],[0,0,0]]
teleports = [((0,2),(2,0))]
print(minSteps(grid, (0,0), (2,2), teleports))
