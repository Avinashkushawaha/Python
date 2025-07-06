def all_paths_source_target(graph):
    res = []
    def dfs(node, path):
        if node == len(graph) - 1:
            res.append(path)
            return
        for nei in graph[node]:
            dfs(nei, path + [nei])
    dfs(0, [0])
    return res

print(all_paths_source_target([[1,2],[3],[3],[]]))  # [[0,1,3],[0,2,3]]
