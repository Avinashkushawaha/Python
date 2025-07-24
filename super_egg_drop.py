def superEggDrop(k, n):
    memo = {}
    def dp(k, n):
        if k == 1: return n
        if n == 0: return 0
        if (k, n) in memo:
            return memo[(k, n)]
        low, high = 1, n
        res = n
        while low <= high:
            mid = (low + high) // 2
            broken = dp(k - 1, mid - 1)
            not_broken = dp(k, n - mid)
            if broken > not_broken:
                high = mid - 1
                res = min(res, broken + 1)
            else:
                low = mid + 1
                res = min(res, not_broken + 1)
        memo[(k, n)] = res
        return res
    return dp(k, n)
