from collections import deque
def longestSubarray(nums, limit):
    maxdq, mindq = deque(), deque()
    l = ans = 0
    for r, x in enumerate(nums):
        while maxdq and x > maxdq[-1]: maxdq.pop()
        while mindq and x < mindq[-1]: mindq.pop()
        maxdq.append(x); mindq.append(x)
        while maxdq[0] - mindq[0] > limit:
            if nums[l] == maxdq[0]: maxdq.popleft()
            if nums[l] == mindq[0]: mindq.popleft()
            l += 1
        ans = max(ans, r - l + 1)
    return ans


