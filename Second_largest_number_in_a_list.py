def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print(second_largest([1, 5, 2, 8, 3, 8]))