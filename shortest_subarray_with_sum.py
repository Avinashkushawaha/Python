from collections import deque
def shortestSubarray(nums, K):
    n = len(nums)
    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1] = pref[i] + nums[i]
    ans = n+1
    dq = deque()
    for i in range(n+1):
        while dq and pref[i] - pref[dq[0]] >= K:
            ans = min(ans, i - dq.popleft())
        while dq and pref[i] <= pref[dq[-1]]:
            dq.pop()
        dq.append(i)
    return ans if ans <= n else -1

# print(shortestSubarray([2,-1,2], 3))  # 3
