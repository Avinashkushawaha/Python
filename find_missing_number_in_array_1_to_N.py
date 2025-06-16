def missing_number(arr, n):
    return n * (n + 1) // 2 - sum(arr)

print(missing_number([1, 2, 4, 5], 5))