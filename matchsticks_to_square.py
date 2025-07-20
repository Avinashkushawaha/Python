def makesquare(matchsticks):
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    side = total // 4
    matchsticks.sort(reverse=True)

    sides = [0] * 4

    def dfs(index):
        if index == len(matchsticks):
            return all(s == side for s in sides)
        for i in range(4):
            if sides[i] + matchsticks[index] <= side:
                sides[i] += matchsticks[index]
                if dfs(index + 1): return True
                sides[i] -= matchsticks[index]
        return False

    return dfs(0)
