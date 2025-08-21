class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        self.parent[py] = px
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst, cost = [], 0
    edges.sort(key=lambda x: x[2])  # sort by weight
    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            cost += w
    return cost, mst

edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
print(kruskal(4, edges))  
# Output: (19, [(2, 3, 4), (0, 3, 5), (0, 1, 10)])
