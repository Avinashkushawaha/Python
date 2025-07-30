from collections import deque

def cutOffTree(forest):
    def bfs(sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return 0
        R, C = len(forest), len(forest[0])
        visited = [[False]*C for _ in range(R)]
        q = deque([(sx, sy, 0)])
        visited[sx][sy] = True
        while q:
            x, y, d = q.popleft()
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and forest[nx][ny] > 0:
                    if nx == tx and ny == ty:
                        return d+1
                    visited[nx][ny] = True
                    q.append((nx, ny, d+1))
        return -1

    trees = sorted((val, i, j) for i, row in enumerate(forest) for j, val in enumerate(row) if val > 1)
    total = 0
    x = y = 0
    for h, i, j in trees:
        d = bfs(x, y, i, j)
        if d == -1:
            return -1
        total += d
        x, y = i, j
    return total
