def sliding_window_sum(arr, k):
    Window_sum = sum(arr[:k])
    result = [Window_sum]
    for i in range(k, len(arr)):
        Window_sum += arr[i] - arr[i - k]
        result.append(Window_sum)
    return result

print(sliding_window_sum([1, 2, 3, 4, 5], 3))    