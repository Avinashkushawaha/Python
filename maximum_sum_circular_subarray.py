def max_subarray_sum_circular(nums):
    total = sum(nums)
    cur_max = max_sum = nums[0]
    cur_min = min_sum = nums[0]
    for n in nums[1:]:
        cur_max = max(n, cur_max + n)
        max_sum = max(max_sum, cur_max)
        cur_min = min(n, cur_min + n)
        min_sum = min(min_sum, cur_min)
    return max_sum if max_sum < 0 else max(max_sum, total - min_sum)

print(max_subarray_sum_circular([1,-2,3,-2]))  # 3
