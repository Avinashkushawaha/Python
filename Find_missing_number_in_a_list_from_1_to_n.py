def find_missing(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

print(find_missing([1, 2, 4, 5], 5)) 