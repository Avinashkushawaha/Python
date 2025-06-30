def subsets_with_dup(nums):
    res = []
    nums.sort()

    def backtrack(start, path):
        res.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res

print(subsets_with_dup([1,2,2]))
