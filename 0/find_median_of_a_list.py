def find_median(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2
    return (arr[mid] + arr[mid - 1]) / 2

print(find_median([1, 2, 3, 4, 5]))