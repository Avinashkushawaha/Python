def combination_sum(candidates, target):
    res = []

    def backtrack(remain, path, start):
        if remain == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                continue
            path.append(candidates[i])
            backtrack(remain - candidates[i], path, i)
            path.pop()

    backtrack(target, [], 0)
    return res

print(combination_sum([2,3,6,7], 7))  # [[2,2,3],[7]]
