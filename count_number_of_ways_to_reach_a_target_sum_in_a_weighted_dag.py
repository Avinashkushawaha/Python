from collections import defaultdict, deque

def count_paths(n, edges, target):
    graph = defaultdict(list)
    indeg = [0]*n
    for u, v, w in edges:
        graph[u].append((v,w))
        indeg[v]+=1

    dp=[0]*n
    dp[0]=1
    q=deque([i for i in range(n) if indeg[i]==0])
    while q:
        u=q.popleft()
        for v,w in graph[u]:
            dp[v]+=dp[u]
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    return dp[target]

print(count_paths(5, [(0,1,1),(1,2,1),(0,2,1),(2,3,1),(3,4,1)], 4))  # 2
