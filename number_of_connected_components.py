def count_components(n, edges):
    parent = list(range(n))

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for u, v in edges:
        union(u, v)

    return len(set(find(i) for i in range(n)))

print(count_components(5, [[0,1],[1,2],[3,4]]))  # 2
