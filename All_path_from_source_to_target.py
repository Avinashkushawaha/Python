def allPathsSourceTarget(graph):
    res = []
    def dfs(path, node):
        if node == len(graph) - 1:
            res.append(list(path))
            return
        for nei in graph[node]:
            dfs(path + [nei], nei)
    dfs([0], 0)
    return res
