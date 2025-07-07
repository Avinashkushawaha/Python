from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0]*n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return topo if len(topo) == n else []

print(topo_sort(4, [(0,1),(0,2),(1,2),(2,3)]))  # [0,1,2,3]
