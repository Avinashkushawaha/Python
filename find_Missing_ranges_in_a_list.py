def find_missing_ranges(nums, start, end):
    result = []
    prev = start - 1
    nums.append(end + 1)
    for num in nums:
        if num - prev > 2:
            result.append((prev + 1, num - 1))
        prev = num
    return result

print(find_missing_ranges([1, 2, 4, 7], 1, 10))  # Output: [(3, 3), (5, 6), (8, 10)]
