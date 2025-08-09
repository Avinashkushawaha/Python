from collections import defaultdict

class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        
        ans = [-1] * n
        
        def dfs(x):
            if ans[x] != -1:
                return ans[x]
            ans[x] = x
            for nei in graph[x]:
                cand = dfs(nei)
                if quiet[cand] < quiet[ans[x]]:
                    ans[x] = cand
            return ans[x]
        
        for i in range(n):
            dfs(i)
        return ans
