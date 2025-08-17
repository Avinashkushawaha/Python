def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([2, 3, 2, 4, 4]))  # 3
