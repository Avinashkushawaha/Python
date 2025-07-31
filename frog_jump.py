def canCross(stones):
    stone_set = set(stones)
    last_stone = stones[-1]
    dp = {s: set() for s in stones}
    dp[0].add(0)
    
    for s in stones:
        for k in dp[s]:
            for step in [k-1, k, k+1]:
                if step > 0 and s+step in stone_set:
                    dp[s+step].add(step)
                    
    return bool(dp[last_stone])
