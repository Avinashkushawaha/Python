def subset_sum(nums, target):
    res = [] 
    def backtrack(start, path, total):
        if total == target:
            res.append(path)
            return 
        for i in range(start, len(nums)):
            if total + nums[i] <= target:
                backtrack(i + 1, path + [nums[i]], total + nums[i])
    backtrack(0, [], 0)
    return res 
print(subset_sum([1, 2, 3, 4, 5], 5))  