def max_product(nums):
    max_prod = min_prod = res = nums[0]
    for n in nums[1:]:
        temp = max(n, n * max_prod, n * min_prod)
        min_prod = min(n, n * max_prod, n * min_prod)
        max_prod = temp
        res = max(res, max_prod)
    return res

print(max_product([2,3,-2,4]))  # 6
