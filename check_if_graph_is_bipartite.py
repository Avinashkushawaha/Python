def is_bipartite(graph):
    color = {}
    def dfs(node, c):
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(nei, c ^ 1) for nei in graph[node])
    return all(dfs(i, 0) for i in range(len(graph)) if i not in color)

print(is_bipartite([[1,3],[0,2],[1,3],[0,2]]))  # True
