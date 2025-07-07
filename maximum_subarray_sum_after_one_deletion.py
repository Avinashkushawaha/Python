def max_sum_after_deletion(arr):
    max_end_here = max_delete = arr[0]
    res = arr[0]
    for i in range(1, len(arr)):
        max_delete = max(max_end_here, max_delete + arr[i])
        max_end_here = max(arr[i], max_end_here + arr[i])
        res = max(res, max_delete)
    return res

print(max_sum_after_deletion([1,-2,0,3]))  # 4
