from collections import deque
def sliding_window_maximum(nums, k):
    dq, res = deque(), []
    for i, n in enumerate(nums):
        while dq and nums [dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res 

print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]                