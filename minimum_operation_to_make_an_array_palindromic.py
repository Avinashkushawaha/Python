def minOpsToPalindrome(arr):
    i, j = 0, len(arr) - 1
    ops = 0
    while i < j:
        if arr[i] < arr[j]:
            arr[i+1] += arr[i]
            ops += 1
            i += 1
        elif arr[i] > arr[j]:
            arr[j-1] += arr[j]
            ops += 1
            j -= 1
        else:
            i += 1
            j -= 1
    return ops

print(minOpsToPalindrome([1, 4, 5, 9, 1]))  # Example
