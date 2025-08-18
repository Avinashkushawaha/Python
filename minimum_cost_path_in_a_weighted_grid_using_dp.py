import heapq

def min_cost(grid):
    n,m=len(grid),len(grid[0])
    dist=[[float("inf")]*m for _ in range(n)]
    dist[0][0]=grid[0][0]
    pq=[(grid[0][0],0,0)]
    while pq:
        d,x,y=heapq.heappop(pq)
        if (x,y)==(n-1,m-1):
            return d
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                nd=d+grid[nx][ny]
                if nd<dist[nx][ny]:
                    dist[nx][ny]=nd
                    heapq.heappush(pq,(nd,nx,ny))

grid=[[1,3,1],[1,5,1],[4,2,1]]
print(min_cost(grid))  # 7
