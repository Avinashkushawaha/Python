def sumOfDistancesInTree(n, edges):
    from collections import defaultdict
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    res = [0] * n
    count = [1] * n

    def dfs(node, parent):
        for nei in tree[node]:
            if nei != parent:
                dfs(nei, node)
                count[node] += count[nei]
                res[node] += res[nei] + count[nei]

    def dfs2(node, parent):
        for nei in tree[node]:
            if nei != parent:
                res[nei] = res[node] - count[nei] + (n - count[nei])
                dfs2(nei, node)

    dfs(0, -1)
    dfs2(0, -1)
    return res
