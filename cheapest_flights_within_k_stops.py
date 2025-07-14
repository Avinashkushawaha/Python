import heapq
from collections import defaultdict

def find_cheapest_price(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    heap = [(0, src, k + 1)]
    while heap:
        cost, u, stops = heapq.heappop(heap)
        if u == dst:
            return cost
        if stops > 0:
            for v, w in graph[u]:
                heapq.heappush(heap, (cost + w, v, stops - 1))
    return -1
