from collections import defaultdict

def longest_path(n, edges):
    graph = defaultdict(list)
    indeg=[0]*n
    for u,v in edges:
        graph[u].append(v)
        indeg[v]+=1

    topo=[]
    stack=[i for i in range(n) if indeg[i]==0]
    while stack:
        u=stack.pop()
        topo.append(u)
        for v in graph[u]:
            indeg[v]-=1
            if indeg[v]==0:
                stack.append(v)

    dp=[0]*n
    for u in topo:
        for v in graph[u]:
            dp[v]=max(dp[v],dp[u]+1)
    return max(dp)

print(longest_path(6, [(0,1),(0,2),(1,3),(2,3),(3,4),(4,5)]))  # 5
