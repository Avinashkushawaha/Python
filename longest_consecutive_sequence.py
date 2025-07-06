def longest_consecutive(nums):
    nums_set = set(nums)
    max_len = 0
    for num in nums:
        if num - 1 not in nums_set:
            curr = num
            while curr in nums_set:
                curr += 1
            max_len = max(max_len, curr - num)
    return max_len

print(longest_consecutive([100,4,200,1,3,2]))  # 4
