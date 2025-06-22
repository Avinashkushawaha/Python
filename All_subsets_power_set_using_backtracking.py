def subsets(nums):
    result = []

    def backtrack(index, path):
        result.append(path)
        for i in range(index, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))        