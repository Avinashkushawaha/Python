import heapq
from collections import defaultdict

def findCheapestPrice(n, flights, src, dst, K):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    heap = [(0, src, K+1)]
    while heap:
        cost, node, stops = heapq.heappop(heap)
        if node == dst:
            return cost
        if stops > 0:
            for nei, price in graph[node]:
                heapq.heappush(heap, (cost + price, nei, stops - 1))
    return -1
