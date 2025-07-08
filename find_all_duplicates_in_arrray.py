def find_duplicates(nums):
    res = []
    for num in nums:
        i = abs(num) - 1
        if nums[i] < 0:
            res.append(abs(num))
        nums[i] *= -1
    return res

print(find_duplicates([4,3,2,7,8,2,3,1]))  # [2, 3]
