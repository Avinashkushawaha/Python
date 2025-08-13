import heapq

def minCostConnectPoints3D(points):
    n = len(points)
    visited = [False] * n
    minHeap = [(0, 0)]  # cost, node
    total = 0
    edges = 0

    while edges < n:
        cost, u = heapq.heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        total += cost
        edges += 1
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1]) + abs(points[u][2]-points[v][2])
                heapq.heappush(minHeap, (dist, v))
    return total

print(minCostConnectPoints3D([[0,0,0],[1,2,3],[4,5,6],[7,8,9]]))
