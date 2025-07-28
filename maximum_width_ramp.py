def maxWidthRamp(nums):
    stack = []
    for i, v in enumerate(nums):
        if not stack or nums[stack[-1]] > v:
            stack.append(i)

    res = 0
    for j in reversed(range(len(nums))):
        while stack and nums[stack[-1]] <= nums[j]:
            res = max(res, j - stack.pop())
    return res
