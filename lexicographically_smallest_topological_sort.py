from heapq import heappush, heappop
from collections import defaultdict

def lexTopoSort(n, edges):
    indeg = [0] * n
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1

    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heappush(heap, i)

    result = []
    while heap:
        u = heappop(heap)
        result.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heappush(heap, v)
    return result if len(result) == n else []
