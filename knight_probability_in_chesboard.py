def knightProbability(n, k, row, col):
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    memo = {}

    def dp(k, r, c):
        if not (0 <= r < n and 0 <= c < n):
            return 0
        if k == 0:
            return 1
        if (k, r, c) in memo:
            return memo[(k, r, c)]
        prob = 0
        for dr, dc in moves:
            prob += dp(k-1, r+dr, c+dc) / 8
        memo[(k, r, c)] = prob
        return prob

    return dp(k, row, col)
