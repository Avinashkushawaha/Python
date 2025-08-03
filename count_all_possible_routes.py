def countRoutes(locations, start, finish, fuel):
    MOD = 10**9 + 7
    from functools import lru_cache
    
    @lru_cache(None)
    def dfs(pos, f):
        if f < 0:
            return 0
        res = 1 if pos == finish else 0
        for nxt in range(len(locations)):
            if nxt != pos:
                cost = abs(locations[pos] - locations[nxt])
                res += dfs(nxt, f - cost)
        return res % MOD
    
    return dfs(start, fuel)
