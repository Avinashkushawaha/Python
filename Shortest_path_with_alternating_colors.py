from collections import deque, defaultdict

def shortestAlternatingPaths(n, redEdges, blueEdges):
    graph = [defaultdict(list), defaultdict(list)]
    for u, v in redEdges: graph[0][u].append(v)
    for u, v in blueEdges: graph[1][u].append(v)
    
    res = [-1] * n
    q = deque([(0,0),(0,1)])
    visited = {(0,0),(0,1)}
    steps = 0
    
    while q:
        for _ in range(len(q)):
            node, color = q.popleft()
            if res[node] == -1: res[node] = steps
            for nei in graph[1-color][node]:
                if (nei,1-color) not in visited:
                    visited.add((nei,1-color))
                    q.append((nei,1-color))
        steps += 1
    return res

print(shortestAlternatingPaths(3, [[0,1],[1,2]], []))
