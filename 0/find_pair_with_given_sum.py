def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False

print(has_pair_with_sum([10, 15, 3, 7], 17))  # True
