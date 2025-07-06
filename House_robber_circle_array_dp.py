def rob(nums):
    def simple_rob(nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + n)
        return rob2

    if len(nums) == 1:
        return nums[0]
    return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

print(rob([2,3,2]))  # 3
